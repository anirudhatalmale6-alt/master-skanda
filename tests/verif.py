# -*- coding: utf-8 -*-
"""
Vérification du site Master Skanda.

Deux natures de contrôle, et la seconde est la seule qui prouve quelque
chose : lire la source dit ce qui a été écrit, mesurer le rendu dit ce que
le navigateur a fait. Les contrastes, les proportions d'images, les
débordements, les ancres et les requêtes réseau sont donc mesurés dans un
Chromium réel, jamais déduits de la feuille de style.

    python3 tests/verif.py [http://127.0.0.1:8873/]
"""

import json
import math
import os
import re
import sys
import io

from playwright.sync_api import sync_playwright
from PIL import Image

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI)
sys.path.insert(0, os.path.join(RACINE, "source"))

import contenu as C          # noqa: E402
import build as B            # noqa: E402

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8873/"
if not BASE.endswith("/"):
    BASE += "/"

# 1240 et 1260 encadrent le point de bascule de la signature d'en-tête :
# c'est exactement là que le débordement français de 33 px se produisait.
LARGEURS = [320, 360, 390, 414, 480, 600, 768, 834, 900, 1000, 1001, 1024,
            1180, 1240, 1259, 1260, 1280, 1366, 1440]

ok = 0
echecs = []


def v(cond, nom):
    global ok
    if cond:
        ok += 1
    else:
        echecs.append(nom)


# ---------------------------------------------------------------- motifs
# Chaque motif décrit une AFFIRMATION interdite : un verbe d'état suivi du
# mot. « n'est pas garanti » doit passer, « est garanti » doit échouer.
NEGATIONS = re.compile(
    r"\b(no|not|never|nor|neither|without|cannot|can't|non|ne|n'|ni|"
    r"aucun|aucune|jamais|sans|pas)\b", re.I)

INTERDITS = [
    # promesses
    (r"\b(est|sont|seront)\s+garanti", "promesse : garanti"),
    (r"\b(is|are|will be)\s+guaranteed", "promise: guaranteed"),
    (r"\brésultat[s]?\s+(assuré|garanti)", "promesse : resultat assure"),
    (r"\bguéri(r|son|t)\b", "sante : guerison"),
    (r"\b(cure[sd]?|healing guaranteed)\b", "health: cure"),
    (r"\bretour\s+de\s+l['’]?être\s+aimé", "promesse : retour affectif"),
    # superlatifs invérifiables (article 7.1)
    (r"\ble\s+meilleur\b|\bla\s+meilleure\b", "superlatif : le meilleur"),
    (r"\bthe\s+best\b", "superlative: the best"),
    (r"\b100\s*%\b", "superlatif : 100 %"),
    (r"\b(numéro un|number one|n°\s?1)\b", "superlatif : numero un"),
    # statuts non démontrés
    (r"\b(est|sont)\s+(certifié|diplômé|accrédité|agréé|reconnu)",
     "statut : certifie"),
    (r"\b(is|are)\s+(certified|accredited|licensed|recognised|recognized)",
     "status: certified"),
    # chiffres non fournis
    (r"\b\d+\s*(ans|années)\s+d['’]expérience", "chiffre : annees"),
    (r"\b\d+\s*years?\s+of\s+experience", "figure: years"),
    (r"[$€£]\s?\d|\b\d+\s?(CAD|USD|dollars?)\b", "chiffre : prix"),
    (r"\b\d[.,]\d\s*(/\s*5|étoiles|stars)\b", "chiffre : note"),
    (r"\b\d+\s+(avis|reviews)\b", "chiffre : nombre d'avis"),
    # horaires inventés
    (r"\b(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\b",
     "horaire : jour"),
    (r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b",
     "schedule: day"),
    (r"\b\d{1,2}\s?h\s?\d{2}\b|\b\d{1,2}:\d{2}\s?(am|pm)\b",
     "horaire : heure"),
    # noms de personnes réelles : la consigne du client était une
    # inspiration visuelle, pas une dédicace. Aucun nom ne doit apparaître.
    (r"\btrump\b", "nom de personne reelle"),
    (r"\bivana\b", "nom de personne reelle"),
    (r"\btaj\s*mahal\b", "monument reel nomme comme reference"),
]

# Mesure et suivi : le site n'en embarque aucun.
MESURE = re.compile(
    r"gtag\(|googletagmanager|google-analytics|matomo\.js|plausible\.io|"
    r"facebook\.net|hotjar|clarity\.ms|<script[^>]*analytic", re.I)


def touches(motif, txt):
    """Retourne les occurrences NON niées et NON interrogatives d'un motif.

    Deux portées, et il a fallu les deux.

    1. La négation gouverne sa PHRASE, pas un nombre arbitraire de
       caractères : « Neither the designation nor ... is accredited » place
       le « Neither » à soixante-dix caractères du mot visé.

    2. Une QUESTION n'est pas une affirmation. « Est-ce que les résultats
       sont garantis ? — Non, et ils ne peuvent pas l'être. » : le motif
       tombe dans l'interrogation, la négation est dans la phrase suivante,
       et un contrôle qui ne regarde que vers l'arrière la manque. On lit
       donc aussi la fin de la phrase.
    """
    out = []
    for m in re.finditer(motif, txt, re.I):
        deb = max((txt.rfind(c, 0, m.start()) for c in ".!?;\n"), default=-1)
        fins = [p for p in (txt.find(c, m.end()) for c in ".!?;\n") if p >= 0]
        fin = min(fins) if fins else len(txt)
        avant = txt[deb + 1:m.start()]
        if NEGATIONS.search(avant):
            continue
        if txt[fin:fin + 1] == "?":
            continue
        out.append(m.group(0))
    return out


def sans_balises(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h,
               flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = h.replace("&nbsp;", " ").replace("&mdash;", "—")
    h = h.replace("&amp;", "&").replace("&laquo;", "«").replace("&raquo;", "»")
    h = h.replace("&#9742;", " ").replace("&quot;", '"')
    return re.sub(r"\s+", " ", h)


# ----------------------------------------------------- contraste mesuré
def luminance(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(rgb[0]) + 0.7152 * f(rgb[1]) + 0.0722 * f(rgb[2])


def contraste(a, b):
    la, lb = luminance(a), luminance(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def couleur_css(s):
    m = re.findall(r"[\d.]+", s or "")
    if len(m) < 3:
        return None
    return (int(float(m[0])), int(float(m[1])), int(float(m[2])))


def contraste_mesure(pg, selecteur):
    """Contraste réel du texte d'un élément contre ce qui est peint derrière.

    Méthode : rendre le TEXTE transparent, photographier la zone, et
    retenir le pixel de fond le plus défavorable.

    Deux corrections par rapport à la version précédente, et chacune vient
    d'une lecture fausse.

    * Cacher l'élément entier (`visibility:hidden`) découvre le fond de
      l'ANCÊTRE. Pour un élément qui porte sa propre couleur de fond — un
      bandeau, un badge, un bouton — on mesure alors le texte contre une
      couleur qui n'est jamais visible sous lui. Le bandeau de démonstration
      s'est ainsi mesuré à 1,02:1 alors qu'il vaut 8,74:1. Rendre seulement
      le texte transparent laisse le fond réel en place.

    * Prendre le 98e centile de LUMINANCE suppose que le texte est clair sur
      fond sombre. Pour du texte sombre sur fond clair, le pire cas est le
      pixel le plus SOMBRE, et le 98e centile donnait la réponse la plus
      flatteuse. On classe donc par contraste, pas par luminance, et on
      retient le 2e centile — le pire cas, à l'abri d'un pixel aberrant.
    """
    infos = pg.evaluate("""(s)=>{const e=document.querySelector(s);
      if(!e) return null; const r=e.getBoundingClientRect();
      if(r.width<4||r.height<4) return null;
      const st=getComputedStyle(e);
      const b=x=>parseFloat(st['border'+x+'Width'])||0;
      return {x:r.x,y:r.y,w:r.width,h:r.height,couleur:st.color,
              bt:b('Top'),br:b('Right'),bb:b('Bottom'),bl:b('Left')};}""",
                        selecteur)
    if not infos:
        return None, None
    fg = couleur_css(infos["couleur"])
    if not fg:
        return None, None
    # on retire les bordures : elles appartiennent à l'élément, pas au fond
    # sur lequel le texte se lit
    mx = infos["bl"] + 2
    my = infos["bt"] + 2
    x = max(0.0, infos["x"] + mx)
    y = max(0.0, infos["y"] + my)
    w = max(4.0, infos["w"] - mx - infos["br"] - 2)
    h = max(4.0, infos["h"] - my - infos["bb"] - 2)

    pg.evaluate("""(s)=>{const e=document.querySelector(s);
      e.dataset.c=e.style.color||''; e.style.setProperty(
        'color','transparent','important');}""", selecteur)
    png = pg.screenshot(clip={"x": x, "y": y, "width": w, "height": h})
    pg.evaluate("""(s)=>{const e=document.querySelector(s);
      e.style.color=e.dataset.c||'';}""", selecteur)

    im = Image.open(io.BytesIO(png)).convert("RGB")
    valeurs = sorted(contraste(fg, px) for px in im.getdata())
    pire = valeurs[max(0, int(len(valeurs) * 0.02) - 1)]
    return pire, fg


# --------------------------------------------------------------- pages
def toutes_les_pages():
    liste = []
    for lg in ("fr", "en"):
        for p in C.PAGES:
            liste.append((p[0], lg, "%s/%s" % (lg, B.fichier(p[0], lg))))
    return liste


PAGES = toutes_les_pages()


# =====================================================================
def section_1_source():
    """Ce que le fichier contient. Ne prouve rien sur le rendu."""
    for cle, lg, rel in PAGES:
        chemin = os.path.join(RACINE, rel)
        h = open(chemin, encoding="utf-8").read()
        nom = "%s [%s]" % (rel, "src")
        v(h.startswith("<!doctype html>"), nom + " doctype")
        v(('<html lang="%s">' % B.HTML_LANG[lg]) in h, nom + " lang")
        v(h.count("<h1") == 1, nom + " un seul h1")
        v('id="principal"' in h, nom + " cible du lien d'evitement")
        v('class="saut"' in h, nom + " lien d'evitement")
        v('rel="canonical"' in h, nom + " canonical")
        v(h.count('rel="alternate" hreflang=') == 3, nom + " hreflang x3")
        v('name="robots" content="noindex' in h, nom + " noindex (demo)")
        v("favicon.svg" in h, nom + " favicon")
        m = re.search(r'name="description" content="([^"]*)"', h)
        v(m and 40 < len(m.group(1)) < 320, nom + " longueur description")
        v(not MESURE.search(h), nom + " aucun outil de mesure")
        # une ressource chargée depuis un tiers
        tiers = re.findall(r'(?:src|href)="(https?://[^"]+)"', h)
        tiers = [u for u in tiers
                 if not u.startswith(("https://schema.org",
                                      "http://www.w3.org",
                                      "https://www.sitemaps.org",
                                      "https://anirudhatalmale6-alt.github.io",
                                      C.LIEN_FICHE))]
        v(not tiers, nom + " aucune ressource tierce %s" % tiers[:1])
        # le texte visible
        txt = sans_balises(h)
        for motif, etiquette in INTERDITS:
            hits = touches(motif, txt)
            v(not hits, "%s : %s %s" % (rel, etiquette, hits[:2]))
        # Le badge d'attente porte toujours EXACTEMENT le mot du projet, et
        # jamais celui d'un autre chantier. (Le premier contrôle écrit ici
        # exigeait l'inverse — qu'aucune page ne contienne le mot sans le
        # badge — et il échouait sur des phrases parfaitement correctes du
        # genre « tarifs à confirmer ». Un contrôle qui punit la prose n'a
        # pas trouvé un défaut, il en est un.)
        mot = C.ATTENTE[0] if lg == "fr" else C.ATTENTE[1]
        for texte in re.findall(r'<span class="att">([^<]*)</span>', h):
            v(texte == mot, "%s : badge d'attente « %s »" % (rel, texte))
        # Le vocabulaire d'attente d'un autre chantier ne doit pas servir
        # d'ÉTIQUETTE ici. On cherche donc un nœud de texte entier, pas une
        # sous-chaîne : « what remains to be decided » est de la prose
        # anglaise ordinaire, et un contrôle qui la refuse se trompe de
        # cible — c'est la deuxième fois dans ce fichier.
        for autre in ("à vérifier", "à définir", "To be decided",
                      "En attente d'autorisation", "Awaiting authorisation"):
            seul = re.search(r">\s*%s\s*<" % re.escape(autre), h, re.I)
            v(not seul, "%s : etiquette d'attente d'un autre projet (%s)"
              % (rel, autre))


def section_2_liens():
    """Aucun lien mort, et l'aller-retour de langue revient au point de
    départ."""
    connus = set(rel for _, _, rel in PAGES)
    connus.add("index.html")
    for cle, lg, rel in PAGES:
        h = open(os.path.join(RACINE, rel), encoding="utf-8").read()
        dossier = os.path.dirname(rel)
        for href in re.findall(r'href="([^"#:]+\.html)(?:#[^"]*)?"', h):
            cible = os.path.normpath(os.path.join(dossier, href))
            v(cible.replace(os.sep, "/") in connus,
              "%s : lien mort %s" % (rel, href))
        # aller-retour de langue
        autre = "en" if lg == "fr" else "fr"
        attendu = "../%s/%s" % (autre, B.fichier(cle, autre))
        v(('class="langue" href="%s"' % attendu) in h,
          "%s : bascule de langue vers la page equivalente" % rel)


def section_3_plan():
    plan = open(os.path.join(RACINE, "sitemap.xml"), encoding="utf-8").read()
    for cle, lg, rel in PAGES:
        v(("/%s</loc>" % rel) in plan or ("/" + rel) in plan,
          "sitemap : %s present" % rel)
    rob = open(os.path.join(RACINE, "robots.txt"), encoding="utf-8").read()
    v("Disallow: /" in rob, "robots : demo interdite d'indexation")
    v(os.path.isfile(os.path.join(RACINE, "index.html")),
      "aiguillage a la racine")


# =====================================================================
def section_4_rendu(pg, journal):
    """Ce que le navigateur fait vraiment, à quatorze largeurs."""
    for cle, lg, rel in PAGES:
        journal["erreurs"] = []
        journal["externes"] = []
        pg.goto(BASE + rel, wait_until="networkidle")
        pg.wait_for_timeout(120)
        nom = rel

        v(not journal["erreurs"],
          "%s : aucune erreur console %s" % (nom, journal["erreurs"][:1]))
        # Une requête sortante trahirait la page Confidentialité, qui
        # affirme le contraire. C'est mesuré, pas supposé.
        v(not journal["externes"],
          "%s : aucune requete hors domaine %s" % (nom,
                                                   journal["externes"][:1]))
        v(pg.evaluate("document.fonts.status") == "loaded",
          "%s : polices chargees" % nom)

        for w in LARGEURS:
            pg.set_viewport_size({"width": w, "height": 820})
            pg.wait_for_timeout(45)
            deb = pg.evaluate(
                "document.documentElement.scrollWidth"
                " - document.documentElement.clientWidth")
            v(deb <= 1, "%s @%d : aucun debordement horizontal (%s)"
              % (nom, w, deb))

        pg.set_viewport_size({"width": 1280, "height": 820})
        pg.wait_for_timeout(60)

        # images : cassées, et boîtes de proportions fausses
        etat = pg.evaluate("""()=>{
          const out={casse:[],boite:[]};
          document.querySelectorAll('img').forEach(i=>{
            if(!i.complete||i.naturalWidth===0){out.casse.push(i.src);return;}
            const r=i.getBoundingClientRect();
            if(r.width<2||r.height<2) return;
            const a=r.width/r.height, b=i.naturalWidth/i.naturalHeight;
            if(Math.abs(a/b-1)>0.02) out.boite.push(
              i.getAttribute('src')+' '+a.toFixed(3)+' vs '+b.toFixed(3));
          });
          return out;}""")
        v(not etat["casse"], "%s : aucune image cassee %s"
          % (nom, etat["casse"][:1]))
        v(not etat["boite"], "%s : aucune boite d'image deformee %s"
          % (nom, etat["boite"][:1]))

        # hiérarchie des titres : jamais de saut de niveau
        saut = pg.evaluate("""()=>{
          let prec=0, mauvais=[];
          document.querySelectorAll('h1,h2,h3,h4').forEach(h=>{
            const n=+h.tagName[1];
            if(prec && n>prec+1) mauvais.push(h.tagName+' '+
              h.textContent.trim().slice(0,26));
            prec=n;});
          return mauvais;}""")
        v(not saut, "%s : hierarchie des titres %s" % (nom, saut[:1]))

        # rien hors de l'écran, hors décor explicitement caché
        hors = pg.evaluate("""()=>{
          const out=[];
          document.querySelectorAll('body *').forEach(e=>{
            if(e.closest('[aria-hidden="true"]')) return;
            const st=getComputedStyle(e);
            if(st.display==='none'||st.visibility==='hidden') return;
            if(e.classList.contains('saut')) return;
            const r=e.getBoundingClientRect();
            if(r.width<1||r.height<1) return;
            if(r.right>document.documentElement.clientWidth+1.5||r.left<-1.5)
              out.push(e.tagName+'.'+(e.className||'').toString().slice(0,22));
          });
          return out;}""")
        v(not hors, "%s : rien hors ecran %s" % (nom, hors[:2]))


def section_5_ancres(pg):
    """Une ancre qui atterrit sous l'en-tête collant est une ancre cassée,
    et ça ne se voit qu'à la largeur où l'en-tête est le plus haut."""
    cibles = [("fr/services.html", "#attente"),
              ("fr/prendre-rendez-vous.html", "#attente"),
              ("en/approach-and-ethics.html", "#nest-pas"),
              ("fr/accessibilite.html", "#pas-fait")]
    for w in (390, 1280):
        for rel, anc in cibles:
            pg.set_viewport_size({"width": w, "height": 780})
            pg.goto(BASE + rel + anc, wait_until="networkidle")
            pg.wait_for_timeout(220)
            y = pg.evaluate("""(a)=>{const e=document.querySelector(a);
              if(!e) return null;
              const h=document.querySelector('.hdr').getBoundingClientRect();
              return e.getBoundingClientRect().top - h.bottom;}""", anc)
            v(y is not None and y >= -1,
              "%s%s @%d : la cible ne passe pas sous l'en-tete (%s)"
              % (rel, anc, w, None if y is None else round(y)))


def section_6_clavier(pg):
    pg.set_viewport_size({"width": 1280, "height": 820})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    pg.keyboard.press("Tab")
    prem = pg.evaluate("document.activeElement.className")
    v("saut" in (prem or ""), "premier tabulateur : lien d'evitement")
    visible = pg.evaluate("""()=>{const e=document.querySelector('.saut');
      return e.getBoundingClientRect().top > -20;}""")
    v(visible, "le lien d'evitement devient visible au focus")
    contour = pg.evaluate("""()=>{const e=document.querySelector('.saut');
      const s=getComputedStyle(e); return s.outlineStyle;}""")
    v(contour not in ("none", None), "contour de focus visible")

    # burger : ouverture, Echap, et cohérence au-delà de 1000 px
    pg.set_viewport_size({"width": 390, "height": 780})
    pg.wait_for_timeout(80)
    pg.click(".burger")
    v(pg.get_attribute(".burger", "aria-expanded") == "true",
      "burger : aria-expanded passe a true")
    v(pg.is_visible(".panneau-nav nav a"), "burger : la navigation apparait")
    pg.keyboard.press("Escape")
    v(pg.get_attribute(".burger", "aria-expanded") == "false",
      "burger : Echap referme")
    pg.click(".burger")
    pg.set_viewport_size({"width": 1280, "height": 820})
    pg.wait_for_timeout(160)
    v(pg.get_attribute(".burger", "aria-expanded") == "false",
      "burger : l'attribut ne ment pas une fois le panneau masque")


def section_7_formulaire(pg):
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.goto(BASE + "fr/prendre-rendez-vous.html", wait_until="networkidle")
    pg.click(".formulaire button[type=submit]")
    pg.wait_for_timeout(120)
    n = pg.evaluate(
        "document.querySelectorAll('.erreur:not(:empty)').length")
    v(n >= 4, "formulaire vide : %d erreurs annoncees" % n)
    focus = pg.evaluate("document.activeElement.id")
    v(focus == "c-prenom", "formulaire : le focus va au premier champ fautif")
    v(pg.evaluate("document.getElementById('form-etat').textContent") == "",
      "formulaire : aucun message de succes quand il est invalide")

    pg.fill("#c-prenom", "Alex")
    pg.fill("#c-contact", "514 000 0000")
    pg.select_option("#c-langue", "fr")
    pg.select_option("#c-service", "svc-affaires")
    pg.check("#k-traitement")
    pg.click(".formulaire button[type=submit]")
    pg.wait_for_timeout(120)
    etat = pg.evaluate(
        "document.getElementById('form-etat').textContent")
    v("branch" in etat, "formulaire valide : l'etat dit que rien n'est envoye")
    v(C.TEL_AFFICHE in etat,
      "formulaire valide : le numero de repli est celui des pages")
    v(pg.evaluate(
        "document.getElementById('k-marketing').checked") is False,
      "consentement marketing jamais coche d'avance")
    v(pg.evaluate("""()=>{const t=document.getElementById('c-message');
        return t && t.getAttribute('maxlength')==='400';}"""),
      "le champ libre est borne")


def section_8_langue(pg):
    """Aller en anglais puis revenir doit ramener à la même page."""
    for cle in ("services", "apropos", "reserver", "avis"):
        depart = "fr/" + B.fichier(cle, "fr")
        pg.set_viewport_size({"width": 1280, "height": 820})
        pg.goto(BASE + depart, wait_until="networkidle")
        pg.click(".langue")
        pg.wait_for_load_state("networkidle")
        v(pg.url.endswith("en/" + B.fichier(cle, "en")),
          "bascule %s -> anglais (%s)" % (cle, pg.url.split("/")[-1]))
        pg.click(".langue")
        pg.wait_for_load_state("networkidle")
        v(pg.url.endswith(depart), "retour %s -> francais" % cle)


def section_9_contraste(pg):
    """Les couleurs telles que l'écran les produit, pas telles que la
    feuille de style les déclare."""
    cas = [
        ("fr/index.html", 1280, ".heros h1", 4.5, "titre du heros"),
        ("fr/index.html", 390, ".heros h1", 4.5, "titre du heros (mobile)"),
        ("fr/index.html", 1280, ".heros .chapo", 4.5, "chapo du heros"),
        ("fr/index.html", 1280, ".util .tel", 4.5, "telephone de la barre"),
        ("fr/index.html", 1280, ".panneau-nav nav a", 4.5, "lien de menu"),
        ("fr/index.html", 1280, ".carte p", 4.5, "texte de carte"),
        ("fr/index.html", 1280, ".pied address", 4.5, "adresse du pied"),
        ("fr/index.html", 1280, ".bandeau-demo", 4.5, "bandeau de demo"),
        ("fr/services.html", 1280, ".liste-attente .att", 4.5,
         "mot de l'attente"),
        ("fr/services.html", 1280, ".liste-attente .cond", 4.5,
         "condition de l'attente"),
        ("fr/services.html", 1280, ".prudence .majeurs", 4.5,
         "mention majeurs"),
        ("fr/prendre-rendez-vous.html", 1280, ".champ .aide", 4.5,
         "aide de champ"),
        ("fr/prendre-rendez-vous.html", 1280, ".avertissement", 4.5,
         "avertissement du formulaire"),
        ("fr/contact-et-itineraire.html", 1280, ".fil a", 4.5,
         "fil d'Ariane"),
    ]
    mesures = []
    for rel, w, sel, seuil, etiquette in cas:
        pg.set_viewport_size({"width": w, "height": 900})
        pg.goto(BASE + rel, wait_until="networkidle")
        pg.wait_for_timeout(150)
        pg.evaluate("""(s)=>{const e=document.querySelector(s);
          if(e) e.scrollIntoView({block:'center'});}""", sel)
        pg.wait_for_timeout(120)
        r, fg = contraste_mesure(pg, sel)
        if r is None:
            v(False, "contraste %s : element introuvable" % etiquette)
            continue
        mesures.append((etiquette, w, round(r, 2)))
        v(r >= seuil, "contraste %s @%d : %.2f:1 (seuil %.1f)"
          % (etiquette, w, r, seuil))
    return mesures


def section_10_details(pg):
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.goto(BASE + "fr/questions-frequentes.html", wait_until="networkidle")
    n = pg.evaluate("document.querySelectorAll('.faq details').length")
    v(n == len(C.FAQ), "FAQ : %d questions rendues" % n)
    v(pg.evaluate(
        "document.querySelectorAll('.faq details[open]').length") == 1,
      "FAQ : une seule question ouverte au chargement")
    pg.click(".faq details:nth-of-type(3) summary")
    pg.wait_for_timeout(80)
    v(pg.evaluate(
        "document.querySelectorAll('.faq details[open]').length") == 2,
      "FAQ : une question s'ouvre au clic")
    # la réponse est dans le DOM même fermée : indexable et cherchable
    v(pg.evaluate("""()=>{const d=document.querySelector(
        '.faq details:not([open]) div p'); return !!(d&&d.textContent.length>20)
        ;}"""), "FAQ : les reponses fermees restent dans le document")


def section_11_mouvement(pg):
    ctx = pg.context
    p2 = ctx.new_page()
    p2.emulate_media(reduced_motion="reduce")
    p2.set_viewport_size({"width": 1280, "height": 820})
    p2.goto(BASE + "fr/index.html", wait_until="networkidle")
    d = p2.evaluate("""()=>{const e=document.querySelector('.faq summary')
        ||document.querySelector('.btn');
      return getComputedStyle(e).transitionDuration;}""")
    # Chromium rend « 1e-06s » et non « 0.001ms » : comparer la CHAÎNE fait
    # échouer un comportement correct. On lit le nombre.
    m = re.match(r"([\d.eE+-]+)(ms|s)", d or "")
    sec = float(m.group(1)) / (1000.0 if m.group(2) == "ms" else 1.0) if m \
        else 9.0
    v(sec < 0.01, "mouvement reduit respecte (%s)" % d)
    p2.close()


def section_12_impression(pg):
    p2 = pg.context.new_page()
    p2.set_viewport_size({"width": 1280, "height": 900})
    p2.goto(BASE + "fr/contact-et-itineraire.html", wait_until="networkidle")
    p2.emulate_media(media="print")
    p2.wait_for_timeout(80)
    cache = p2.evaluate("""()=>{
      const q=s=>{const e=document.querySelector(s);
        return e?getComputedStyle(e).display:'absent';};
      return [q('.util'),q('.hdr'),q('.barre-mobile')];}""")
    v(all(c in ("none", "absent") for c in cache),
      "impression : chrome de navigation retire %s" % cache)
    p2.close()


def section_13_barre_mobile(pg):
    """La barre d'actions ne doit jamais masquer la fin du contenu."""
    for w in (320, 390, 480, 760):
        pg.set_viewport_size({"width": w, "height": 720})
        pg.goto(BASE + "fr/index.html", wait_until="networkidle")
        pg.wait_for_timeout(120)
        r = pg.evaluate("""()=>{
          const b=document.querySelector('.barre-mobile');
          const st=getComputedStyle(b);
          const pb=parseFloat(getComputedStyle(document.body).paddingBottom);
          return {aff:st.display, h:b.getBoundingClientRect().height, pb:pb};}
        """)
        v(r["aff"] == "flex", "barre mobile @%d : affichee" % w)
        v(r["pb"] >= r["h"] - 1,
          "barre mobile @%d : le corps reserve sa hauteur (%.0f >= %.0f)"
          % (w, r["pb"], r["h"]))
        # elle est au-dessus du pied, pas par-dessus son dernier texte
        pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        pg.wait_for_timeout(180)
        chevauche = pg.evaluate("""()=>{
          const b=document.querySelector('.barre-mobile')
            .getBoundingClientRect();
          const p=document.querySelector('.pied .bas p:last-of-type')
            .getBoundingClientRect();
          return p.bottom > b.top + 1;}""")
        v(not chevauche,
          "barre mobile @%d : le dernier texte du pied reste visible" % w)
    pg.set_viewport_size({"width": 1280, "height": 820})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    v(pg.evaluate("""()=>getComputedStyle(
        document.querySelector('.barre-mobile')).display""") == "none",
      "barre mobile : absente sur grand ecran")


# =====================================================================
def main():
    section_1_source()
    section_2_liens()
    section_3_plan()

    journal = {"erreurs": [], "externes": []}
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={"width": 1280, "height": 820})
        pg = ctx.new_page()
        pg.on("console", lambda m: journal["erreurs"].append(m.text)
              if m.type == "error" else None)
        pg.on("pageerror", lambda e: journal["erreurs"].append(str(e)))
        pg.on("request", lambda r: journal["externes"].append(r.url)
              if not r.url.startswith(BASE) and not r.url.startswith("data:")
              else None)

        section_4_rendu(pg, journal)
        section_5_ancres(pg)
        section_6_clavier(pg)
        section_7_formulaire(pg)
        section_8_langue(pg)
        mesures = section_9_contraste(pg)
        section_10_details(pg)
        section_11_mouvement(pg)
        section_12_impression(pg)
        section_13_barre_mobile(pg)
        ctx.close()
        nav.close()

    print("")
    print("contrastes mesures :")
    for e, w, r in mesures:
        print("   %-34s @%-5d %5.2f:1" % (e, w, r))
    print("")
    print("%d controles, %d echecs" % (ok + len(echecs), len(echecs)))
    for e in echecs:
        print("  ECHEC  " + e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
