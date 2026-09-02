# -*- coding: utf-8 -*-
"""
Génère les 30 pages du site (15 en français, 15 en anglais) plus la page
d'aiguillage à la racine, le plan de site et le fichier robots.

À exécuter depuis n'importe où :  python3 source/build.py

DÉMO — tant que DEMO vaut True, chaque page porte un bandeau qui dit que
c'est une démonstration ET une balise robots noindex. Un site de démo qui
publie la vraie adresse et le vrai téléphone d'un commerce ne doit pas
pouvoir être indexé à la place du vrai site. Passer DEMO à False au
lancement retire les deux d'un coup.
"""

import os
import re
import sys

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
sys.path.insert(0, _ICI)

import contenu as C  # noqa: E402

DEMO = True
VERSION_CSS = 1
BASE = "https://anirudhatalmale6-alt.github.io/master-skanda/"

LANGUES = ("fr", "en")
HTML_LANG = {"fr": "fr-CA", "en": "en-CA"}


# ------------------------------------------------------------------ outils
def t(couple, lang):
    """Prend le membre français ou anglais d'un couple."""
    return couple[0] if lang == "fr" else couple[1]


def ech(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def sans_balises(s):
    return re.sub(r"<[^>]+>", "", s)


def page(cle):
    for p in C.PAGES:
        if p[0] == cle:
            return p
    raise KeyError(cle)


def fichier(cle, lang):
    p = page(cle)
    return p[1] if lang == "fr" else p[2]


def titre(cle, lang):
    p = page(cle)
    return p[3] if lang == "fr" else p[4]


def lien(cle, lang, depuis_lang):
    """Lien vers une page. Les deux langues vivent dans des dossiers frères,
    donc un lien inter-langue remonte d'un cran."""
    if lang == depuis_lang:
        return fichier(cle, lang)
    return "../%s/%s" % (lang, fichier(cle, lang))


def actif(cle, courant):
    return ' aria-current="page"' if cle == courant else ""


# --------------------------------------------------------------- fragments
def paras(liste, lang):
    return "\n".join("<p>%s</p>" % t(c, lang) for c in liste)


def cartes(items, lang, niveau="h3"):
    """items : liste de (titre fr, texte fr, titre en, texte en)."""
    o = ['<ul class="g3 cartes">']
    for it in items:
        ti = it[0] if lang == "fr" else it[2]
        tx = it[1] if lang == "fr" else it[3]
        o.append('<li class="carte"><%s>%s</%s><p>%s</p></li>'
                 % (niveau, ti, niveau, tx))
    o.append("</ul>")
    return "\n".join(o)


def liste_simple(items, lang):
    o = ['<ul class="puces">']
    for it in items:
        o.append("<li>%s</li>" % t(it, lang))
    o.append("</ul>")
    return "\n".join(o)


def attentes(items, lang):
    """Le bloc « À confirmer ».

    Chaque ligne porte le mot d'attente ET la condition qui la lèvera. Une
    ligne vide sans condition ne dit pas au lecteur ce qui manque ; elle dit
    seulement qu'on n'a pas fini.
    """
    mot = t(C.ATTENTE, lang)
    o = ['<ul class="liste-attente">']
    for it in items:
        ti = it[0] if lang == "fr" else it[2]
        cd = it[1] if lang == "fr" else it[3]
        o.append('<li><span class="att">%s</span>'
                 '<strong>%s</strong><span class="cond">%s</span></li>'
                 % (mot, ti, cd))
    o.append("</ul>")
    return "\n".join(o)


def prudence(lang):
    return ('<aside class="prudence"><p>%s</p><p class="majeurs">%s</p>'
            "</aside>" % (t(C.PRUDENCE, lang), t(C.MAJEURS, lang)))


def panneau(lang, legende_fr, legende_en, prefixe):
    """Emplacement d'image. Un ornement dessiné, jamais une photo générée."""
    lg = legende_fr if lang == "fr" else legende_en
    return ('<figure class="panneau"><img src="%sassets/fenetre.svg" '
            'alt="" width="420" height="520" aria-hidden="true">'
            "<figcaption>%s</figcaption></figure>" % (prefixe, lg))


def boutons(lang, depuis, principal="reserver"):
    return ('<p class="actions">'
            '<a class="btn btn-or" href="tel:%s">%s %s</a> '
            '<a class="btn btn-nuit" href="%s">%s</a></p>'
            % (C.TEL_LIEN, t(C.APPELER, lang), C.TEL_AFFICHE,
               lien(principal, depuis, depuis), t(C.MENU_CTA, lang)))


def sec(idn, titre_txt, corps, classe=""):
    return ('<section id="%s"%s><h2>%s</h2>\n%s\n</section>'
            % (idn, ' class="%s"' % classe if classe else "",
               titre_txt, corps))


def frise():
    return '<hr class="frise" aria-hidden="true">'


# ------------------------------------------------------------------ entête
def entete(cle, lang, prefixe):
    autre = "en" if lang == "fr" else "fr"
    o = []
    o.append('<a class="saut" href="#principal">%s</a>'
             % ("Aller au contenu" if lang == "fr" else "Skip to content"))
    if DEMO:
        o.append('<p class="bandeau-demo">%s</p>' % t(C.PIED_DECLARATION,
                                                      lang))
    o.append('<div class="util"><div class="dans">')
    o.append('<a class="tel" href="tel:%s"><span aria-hidden="true">&#9742;'
             "</span> %s</a>" % (C.TEL_LIEN, C.TEL_AFFICHE))
    o.append('<span class="lieu">%s</span>' % t(C.METRO, lang))
    o.append('<a class="langue" href="%s" lang="%s" hreflang="%s">%s</a>'
             % (lien(cle, autre, lang), HTML_LANG[autre], HTML_LANG[autre],
                t(C.PIED_LANGUE, autre)))
    o.append("</div></div>")

    o.append('<header class="hdr"><div class="dans">')
    o.append('<a class="marque" href="%s">'
             '<img src="%sassets/marque-or.svg" alt="" width="29" height="36" '
             'aria-hidden="true">'
             '<span class="nom">%s</span>'
             '<span class="base">%s</span></a>'
             % (lien("accueil", lang, lang), prefixe, C.MARQUE,
                t(C.BASELINE, lang)))
    o.append('<button class="burger" type="button" aria-expanded="false" '
             'aria-controls="panneau-nav"><span class="barres" '
             'aria-hidden="true"></span><span class="vh">%s</span></button>'
             % ("Menu" if lang == "fr" else "Menu"))
    o.append('<div class="panneau-nav" id="panneau-nav">')
    o.append('<nav aria-label="%s"><ul>'
             % ("Navigation principale" if lang == "fr"
                else "Main navigation"))
    for p in C.PAGES:
        if not p[5]:
            continue
        if p[0] == "reserver":
            continue
        o.append('<li><a href="%s"%s>%s</a></li>'
                 % (lien(p[0], lang, lang), actif(p[0], cle),
                    t(C.MENU_COURT[p[0]], lang)))
    o.append("</ul></nav>")
    o.append('<a class="btn btn-nuit cta-nav" href="%s"%s>%s</a>'
             % (lien("reserver", lang, lang), actif("reserver", cle),
                t(C.MENU_CTA, lang)))
    o.append("</div></div></header>")
    return "\n".join(o)


def fil(cle, lang):
    if cle == "accueil":
        return ""
    lab = "Fil d'Ariane" if lang == "fr" else "Breadcrumb"
    acc = titre("accueil", lang)
    parents = {"svc-affaires": "services", "svc-carriere": "services",
               "svc-finances": "services", "svc-partenariats": "services"}
    o = ['<nav class="fil" aria-label="%s"><ol>' % lab]
    o.append('<li><a href="%s">%s</a></li>' % (lien("accueil", lang, lang),
                                               acc))
    if cle in parents:
        o.append('<li><a href="%s">%s</a></li>'
                 % (lien(parents[cle], lang, lang), titre(parents[cle], lang)))
    o.append('<li><span aria-current="page">%s</span></li>' % titre(cle, lang))
    o.append("</ol></nav>")
    return "\n".join(o)


def pied(cle, lang, prefixe):
    fr = lang == "fr"
    o = ['<footer class="pied"><div class="dans">']
    o.append('<div class="cols">')

    o.append('<div class="col col-marque">')
    o.append('<img src="%sassets/marque-or-clair.svg" alt="" width="34" '
             'height="42" aria-hidden="true">' % prefixe)
    o.append("<p><strong>%s</strong><br>%s</p>" % (C.MARQUE,
                                                   t(C.BASELINE, lang)))
    o.append('<p class="fiche-nom">%s</p>' % C.NOM_FICHE)
    o.append("</div>")

    o.append('<div class="col"><h2>%s</h2><ul>'
             % ("Consultations" if fr else "Consultations"))
    for k in ("svc-affaires", "svc-carriere", "svc-finances",
              "svc-partenariats"):
        o.append('<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                   titre(k, lang)))
    o.append("</ul></div>")

    o.append('<div class="col"><h2>%s</h2><ul>'
             % ("Le cabinet" if fr else "The practice"))
    for k in ("apropos", "approche", "avis", "faq"):
        o.append('<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                   titre(k, lang)))
    o.append("</ul></div>")

    o.append('<div class="col"><h2>%s</h2><ul>'
             % ("Informations" if fr else "Information"))
    for k in ("contact", "conditions", "confidentialite", "accessibilite"):
        o.append('<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                   titre(k, lang)))
    o.append("</ul></div>")

    o.append('<div class="col col-adresse"><h2>%s</h2>'
             % ("Nous joindre" if fr else "Get in touch"))
    o.append('<p><a class="tel-pied" href="tel:%s">%s</a></p>'
             % (C.TEL_LIEN, C.TEL_AFFICHE))
    o.append("<address>%s<br>%s<br><span>%s</span></address>"
             % (t(C.RUE, lang), t(C.VILLE, lang), t(C.METRO, lang)))
    o.append("</div>")
    o.append("</div>")

    o.append('<div class="bas">')
    o.append("<p>%s</p>" % t(C.PRUDENCE, lang))
    o.append('<p class="mini">%s</p>' % t(C.MAJEURS, lang))
    if DEMO:
        o.append('<p class="mini">%s</p>' % t(C.PIED_DECLARATION, lang))
    o.append("</div></div></footer>")

    o.append('<div class="barre-mobile" aria-hidden="false">'
             '<a class="btn btn-or" href="tel:%s">%s</a>'
             '<a class="btn btn-nuit" href="%s">%s</a></div>'
             % (C.TEL_LIEN, t(C.APPELER, lang),
                lien("reserver", lang, lang), t(C.MENU_CTA_COURT, lang)))
    return "\n".join(o)


def donnees_structurees(lang, prefixe):
    """LocalBusiness — uniquement ce qui est sourcé.

    Pas d'horaires (non confirmés), pas de note ni de nombre d'avis (non
    vérifiés), pas de coordonnées géographiques (non mesurées), pas de zone
    desservie (non définie). Déclarer un horaire faux envoie quelqu'un
    devant une porte fermée ; déclarer une note non vérifiée est pire.
    """
    d = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": C.NOM_FICHE,
        "alternateName": C.MARQUE,
        "description": t(C.META["accueil"], lang),
        "url": BASE + lang + "/",
        "telephone": C.TEL_AFFICHE,
        "image": BASE + "assets/marque-or.svg",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "1485 Rue MacDonald",
            "addressLocality": "Saint-Laurent",
            "addressRegion": "QC",
            "postalCode": "H4L 2A8",
            "addressCountry": "CA",
        },
    }
    import json
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(d, ensure_ascii=False))


# ------------------------------------------------------------- constructeurs
def b_accueil(lang, prefixe):
    fr = lang == "fr"
    o = []
    o.append('<section class="heros"><div class="dans heros-grille">')
    o.append('<div class="heros-texte">')
    o.append('<img class="heros-marque" src="%sassets/marque-or.svg" alt="" '
             'width="72" height="89" aria-hidden="true">' % prefixe)
    o.append("<h1>%s</h1>" % t(C.ACC_TITRE, lang))
    o.append('<p class="chapo">%s</p>' % t(C.ACC_SOUS, lang))
    o.append(boutons(lang, lang))
    o.append('<p class="sous-actions">%s &mdash; %s</p>'
             % (t(C.RUE, lang), t(C.METRO, lang)))
    o.append("</div>")
    o.append('<div class="heros-image">')
    o.append('<img src="%sassets/fenetre.svg" alt="" width="420" '
             'height="520" aria-hidden="true">' % prefixe)
    o.append("</div>")
    o.append("</div></section>")

    o.append('<div class="dans">')
    o.append(sec("intro", "Le cabinet" if fr else "The practice",
                 paras(C.ACC_INTRO, lang) + "\n" +
                 cartes(C.ACC_PILIERS, lang)))
    o.append(frise())

    corps = "<p>%s</p>\n" % t(C.SERVICES_INTRO, lang)
    corps += '<ul class="g2 cartes">'
    for k in ("svc-affaires", "svc-carriere", "svc-finances",
              "svc-partenariats"):
        corps += ('<li class="carte carte-lien"><h3><a href="%s">%s</a></h3>'
                  "<p>%s</p></li>"
                  % (lien(k, lang, lang), titre(k, lang),
                     t(C.SERVICES[k]["resume"], lang)))
    corps += "</ul>"
    corps += '<p class="note">%s</p>' % t(C.SERVICES_NOTE, lang)
    o.append(sec("consultations", "Consultations", corps))
    o.append(frise())

    corps = "<p>%s</p>" % (
        "Le cadre est dit avant, pas après. La page Approche et éthique "
        "détaille ce que la consultation est, ce qu'elle n'est pas, et ce "
        "qui n'est jamais demandé."
        if fr else
        "The framework is stated up front, not afterwards. The Approach and "
        "ethics page sets out what a consultation is, what it is not, and "
        "what is never asked of you.")
    corps += '<p class="actions"><a class="btn btn-ligne" href="%s">%s</a>' \
             "</p>" % (lien("approche", lang, lang), titre("approche", lang))
    corps += prudence(lang)
    o.append(sec("cadre", "Le cadre" if fr else "The framework", corps))
    o.append(frise())

    corps = ('<div class="g2 lieu-bloc"><div>'
             "<address><strong>%s</strong><br>%s<br>%s</address>"
             '<p class="actions"><a class="btn btn-or" href="tel:%s">%s %s'
             "</a></p></div>"
             '<div><p>%s</p><p class="actions">'
             '<a class="btn btn-ligne" href="%s">%s</a></p></div></div>'
             % (t(C.RUE, lang), t(C.VILLE, lang), t(C.METRO, lang),
                C.TEL_LIEN, t(C.APPELER, lang), C.TEL_AFFICHE,
                t(C.CONTACT_CARTE_NOTE, lang),
                lien("contact", lang, lang), titre("contact", lang)))
    o.append(sec("lieu", "Où" if fr else "Where", corps))
    o.append("</div>")
    return "\n".join(o), t(C.META["accueil"], lang)


def b_services(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("services", lang))
    o.append('<p class="chapo">%s</p>' % t(C.SERVICES_INTRO, lang))
    corps = '<ul class="g2 cartes">'
    for k in ("svc-affaires", "svc-carriere", "svc-finances",
              "svc-partenariats"):
        s = C.SERVICES[k]
        corps += ('<li class="carte carte-lien"><h3><a href="%s">%s</a></h3>'
                  "<p>%s</p>"
                  '<p class="mini">%s</p></li>'
                  % (lien(k, lang, lang), titre(k, lang),
                     t(s["resume"], lang),
                     (s["pas"][0][0] if fr else s["pas"][0][1])))
    corps += "</ul>"
    o.append(sec("liste", "Les consultations" if fr else "The consultations",
                 corps))
    o.append(frise())
    o.append(sec("attente", "Ce qui reste à confirmer" if fr
                 else "What remains to be confirmed",
                 "<p>%s</p>" % t(C.SERVICES_NOTE, lang) + "\n"
                 + attentes(C.SERVICE_ATTENTES, lang)))
    o.append(prudence(lang))
    o.append(boutons(lang, lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["services"], lang)


def b_service(cle):
    def f(lang, prefixe):
        fr = lang == "fr"
        s = C.SERVICES[cle]
        o = ['<div class="dans">']
        o.append("<h1>%s</h1>" % titre(cle, lang))
        o.append('<p class="chapo">%s</p>' % t(s["resume"], lang))
        o.append('<div class="g2 service-grille"><div>')
        o.append(sec("situations",
                     "Dans quelles situations" if fr else "When people come",
                     liste_simple(s["situations"], lang)))
        o.append(sec("apporte",
                     "Ce que la consultation peut apporter" if fr
                     else "What a consultation can offer",
                     liste_simple(s["apporte"], lang)))
        o.append(sec("limites",
                     "Ce qu'elle ne remplace pas" if fr
                     else "What it does not replace",
                     liste_simple(s["pas"], lang), classe="limites"))
        o.append("</div><div>")
        o.append(panneau(lang,
                         "Panneau ornemental. Aucune photographie du cabinet "
                         "n'a été fournie, et aucune n'est générée.",
                         "Drawn ornament. No photograph of the practice has "
                         "been provided, and none is generated.", prefixe))
        o.append("</div></div>")
        o.append(frise())
        o.append(sec("attente", "Ce qui reste à confirmer" if fr
                     else "What remains to be confirmed",
                     attentes(C.SERVICE_ATTENTES, lang)))
        o.append(prudence(lang))
        o.append(boutons(lang, lang))
        autres = [k for k in ("svc-affaires", "svc-carriere", "svc-finances",
                              "svc-partenariats") if k != cle]
        corps = '<ul class="puces liens-connexes">'
        for k in autres:
            corps += '<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                       titre(k, lang))
        corps += "</ul>"
        o.append(sec("connexes", "Autres consultations" if fr
                     else "Other consultations", corps))
        o.append("</div>")
        return "\n".join(o), t(C.META[cle], lang)
    return f


def b_apropos(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("apropos", lang))
    o.append('<p class="chapo">%s</p>' % t(C.APROPOS_INTRO, lang))
    o.append('<div class="g2 service-grille"><div>')
    o.append(paras(C.APROPOS_TEXTE, lang))
    o.append("</div><div>")
    o.append(panneau(lang,
                     "Panneau ornemental. Une photographie authentique du "
                     "praticien prendra cette place.",
                     "Drawn ornament. An authentic photograph of the "
                     "practitioner will take this place.", prefixe))
    o.append("</div></div>")
    o.append(frise())
    o.append(sec("attente", "Ce qui manque, et pourquoi" if fr
                 else "What is missing, and why",
                 attentes(C.APROPOS_ATTENTES, lang)))
    o.append(boutons(lang, lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["apropos"], lang)


def b_approche(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("approche", lang))
    o.append('<p class="chapo">%s</p>' % t(C.APPROCHE_INTRO, lang))
    o.append(sec("est", "Ce que c'est" if fr else "What it is",
                 cartes(C.APPROCHE_EST, lang)))
    o.append(frise())
    o.append(sec("nest-pas", "Ce que ce n'est pas" if fr
                 else "What it is not",
                 cartes(C.APPROCHE_NEST_PAS, lang), classe="limites"))
    o.append(frise())
    o.append(sec("donnees", "Vos renseignements" if fr
                 else "Your information",
                 cartes(C.APPROCHE_DONNEES, lang)))
    o.append(prudence(lang))
    o.append(boutons(lang, lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["approche"], lang)


def b_faq(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("faq", lang))
    o.append('<p class="chapo">%s</p>'
             % ("Les réponses qui dépendent d'une décision du propriétaire "
                "sont marquées comme telles plutôt que devinées."
                if fr else
                "Answers that depend on a decision by the owner are marked "
                "as such rather than guessed."))
    o.append('<div class="faq">')
    for i, q in enumerate(C.FAQ):
        qt = q[0] if fr else q[2]
        rp = q[1] if fr else q[3]
        o.append('<details%s><summary><span>%s</span></summary>'
                 "<div><p>%s</p></div></details>"
                 % (" open" if i == 0 else "", qt, rp))
    o.append("</div>")
    o.append(prudence(lang))
    o.append(boutons(lang, lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["faq"], lang)


def b_reserver(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("reserver", lang))
    o.append('<p class="chapo">%s</p>' % t(C.RDV_INTRO, lang))
    o.append('<p class="actions"><a class="btn btn-or gros" href="tel:%s">'
             "%s %s</a></p>" % (C.TEL_LIEN, t(C.APPELER, lang),
                                C.TEL_AFFICHE))
    o.append(frise())

    o.append('<div class="g2 form-grille"><div>')
    o.append('<form class="formulaire" novalidate '
             'aria-describedby="form-note">')
    o.append('<p class="avertissement" id="form-note">%s</p>'
             % t(C.RDV_AVERTISSEMENT, lang))
    for (nom, lfr, len_, typ, requis, afr, aen) in C.CHAMPS:
        lab = lfr if fr else len_
        aide = afr if fr else aen
        req = ' <span class="req" aria-hidden="true">*</span>' if requis \
              else ""
        o.append('<p class="champ">')
        o.append('<label for="c-%s">%s%s</label>' % (nom, lab, req))
        o.append('<span class="aide" id="a-%s">%s</span>' % (nom, aide))
        if typ == "textarea":
            o.append('<textarea id="c-%s" name="%s" rows="4" maxlength="400" '
                     'aria-describedby="a-%s"></textarea>' % (nom, nom, nom))
        elif typ == "select":
            o.append('<select id="c-%s" name="%s" aria-describedby="a-%s"%s>'
                     % (nom, nom, nom, " required" if requis else ""))
            o.append('<option value="">%s</option>'
                     % ("Choisir…" if fr else "Choose…"))
            if nom == "langue":
                for v, vfr, ven in C.LANGUES_CHOIX:
                    o.append('<option value="%s">%s</option>'
                             % (v, vfr if fr else ven))
            else:
                for k in ("svc-affaires", "svc-carriere", "svc-finances",
                          "svc-partenariats"):
                    o.append('<option value="%s">%s</option>'
                             % (k, titre(k, lang)))
                o.append('<option value="autre">%s</option>'
                         % ("Autre" if fr else "Other"))
            o.append("</select>")
        else:
            o.append('<input id="c-%s" name="%s" type="text" '
                     'aria-describedby="a-%s"%s>'
                     % (nom, nom, nom, " required" if requis else ""))
        o.append('<span class="erreur" id="e-%s" role="alert"></span>' % nom)
        o.append("</p>")
    for (nom, cfr, cen, requis) in C.CONSENTEMENTS:
        o.append('<p class="champ case"><label for="k-%s">'
                 '<input id="k-%s" name="%s" type="checkbox"%s> <span>%s'
                 "</span></label>"
                 '<span class="erreur" id="e-%s" role="alert"></span></p>'
                 % (nom, nom, nom, " required" if requis else "",
                    cfr if fr else cen, nom))
    o.append('<p class="lien-conf"><a href="%s">%s</a></p>'
             % (lien("confidentialite", lang, lang),
                titre("confidentialite", lang)))
    o.append('<p class="actions"><button class="btn btn-nuit" type="submit">'
             "%s</button></p>" % ("Envoyer la demande" if fr
                                  else "Send the request"))
    o.append('<p class="etat" id="form-etat" role="status"></p>')
    o.append("</form>")
    o.append("</div><div>")
    o.append(sec("attente", "État du formulaire" if fr else "Form status",
                 attentes(C.RDV_ATTENTES, lang)))
    o.append("</div></div>")
    o.append(prudence(lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["reserver"], lang)


def b_contact(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("contact", lang))
    o.append('<p class="chapo">%s</p>' % t(C.CONTACT_INTRO, lang))
    corps = ('<div class="g2"><div class="bloc-coord">'
             '<p><a class="tel-gros" href="tel:%s">%s</a></p>'
             "<address><strong>%s</strong><br>%s<br><span>%s</span>"
             "</address>"
             '<p class="actions"><a class="btn btn-or" href="tel:%s">%s</a> '
             '<a class="btn btn-ligne" href="%s" rel="noopener noreferrer" '
             'target="_blank">%s</a></p></div>'
             '<div><p>%s</p>'
             '<p class="actions"><a class="btn btn-nuit" href="%s">%s</a></p>'
             "</div></div>"
             % (C.TEL_LIEN, C.TEL_AFFICHE,
                t(C.RUE, lang), t(C.VILLE, lang), t(C.METRO, lang),
                C.TEL_LIEN, t(C.APPELER, lang),
                C.LIEN_FICHE,
                "Itinéraire" if fr else "Directions",
                t(C.CONTACT_CARTE_NOTE, lang),
                lien("reserver", lang, lang), t(C.MENU_CTA, lang)))
    o.append(sec("coordonnees", "Coordonnées" if fr else "Details", corps))
    o.append(frise())
    o.append(sec("attente", "Ce qui reste à confirmer" if fr
                 else "What remains to be confirmed",
                 attentes(C.CONTACT_ATTENTES, lang)))
    o.append(prudence(lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["contact"], lang)


def b_avis(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("avis", lang))
    o.append('<p class="chapo">%s</p>' % t(C.AVIS_INTRO, lang))
    o.append(paras(C.AVIS_TEXTE, lang))
    o.append('<p class="actions"><a class="btn btn-ligne" href="%s" '
             'rel="noopener noreferrer" target="_blank">%s</a></p>'
             % (C.LIEN_FICHE,
                "Voir la fiche publique" if fr
                else "Open the public listing"))
    o.append(boutons(lang, lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["avis"], lang)


def b_confidentialite(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("confidentialite", lang))
    o.append('<p class="chapo">%s</p>' % t(C.CONF_INTRO, lang))
    o.append('<aside class="prudence"><p>%s</p></aside>'
             % t(C.CONF_JURIDIQUE, lang))
    o.append(sec("faits", "Ce qui est vrai aujourd'hui" if fr
                 else "What is true today", cartes(C.CONF_FAITS, lang)))
    o.append(frise())
    o.append(sec("attente", "Ce qui doit être décidé avant la mise en ligne"
                 if fr else "What must be decided before launch",
                 attentes(C.CONF_ATTENTES, lang)))
    o.append("</div>")
    return "\n".join(o), t(C.META["confidentialite"], lang)


def b_conditions(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("conditions", lang))
    o.append('<p class="chapo">%s</p>' % t(C.COND_INTRO, lang))
    o.append(sec("points", "Le cadre" if fr else "The framework",
                 cartes(C.COND_POINTS, lang)))
    o.append(frise())
    o.append(sec("attente", "Ce qui reste à confirmer" if fr
                 else "What remains to be confirmed",
                 attentes(C.COND_ATTENTES, lang)))
    o.append(prudence(lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["conditions"], lang)


def b_accessibilite(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("accessibilite", lang))
    o.append('<p class="chapo">%s</p>' % t(C.ACCESS_INTRO, lang))
    o.append(sec("fait", "Ce qui a été mesuré" if fr
                 else "What has been measured", cartes(C.ACCESS_FAIT, lang)))
    o.append(frise())
    o.append(sec("pas-fait", "Ce qui ne l'a pas été" if fr
                 else "What has not been", cartes(C.ACCESS_PAS_FAIT, lang),
                 classe="limites"))
    o.append('<p class="note">%s</p>'
             % ("Un obstacle rencontré sur ce site peut être signalé par "
                "téléphone ; il sera traité comme une anomalie, pas comme "
                "une préférence."
                if fr else
                "Any barrier found on this site can be reported by phone; it "
                "will be treated as a defect, not as a preference."))
    o.append("</div>")
    return "\n".join(o), t(C.META["accessibilite"], lang)


BATISSEURS = {
    "accueil": b_accueil,
    "services": b_services,
    "svc-affaires": b_service("svc-affaires"),
    "svc-carriere": b_service("svc-carriere"),
    "svc-finances": b_service("svc-finances"),
    "svc-partenariats": b_service("svc-partenariats"),
    "apropos": b_apropos,
    "approche": b_approche,
    "faq": b_faq,
    "reserver": b_reserver,
    "contact": b_contact,
    "avis": b_avis,
    "confidentialite": b_confidentialite,
    "conditions": b_conditions,
    "accessibilite": b_accessibilite,
}


# ------------------------------------------------------------------- gabarit
def gabarit(cle, lang):
    prefixe = "../"
    corps, desc = BATISSEURS[cle](lang, prefixe)
    # Une description trop courte ou trop longue est tronquée ou ignorée par
    # les moteurs. Ça a déjà cassé une livraison, donc c'est une assertion.
    if not 40 < len(desc) < 320:
        raise SystemExit("description %s/%s : %d caracteres"
                         % (cle, lang, len(desc)))
    autre = "en" if lang == "fr" else "fr"
    ttl = titre(cle, lang)
    ttl_complet = ("%s — %s" % (C.MARQUE, t(C.BASELINE, lang))
                   if cle == "accueil" else "%s — %s" % (ttl, C.MARQUE))
    o = ["<!doctype html>", '<html lang="%s">' % HTML_LANG[lang], "<head>",
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,'
         'initial-scale=1">',
         "<title>%s</title>" % ech(ttl_complet),
         '<meta name="description" content="%s">' % ech(desc)]
    if DEMO:
        o.append('<meta name="robots" content="noindex,nofollow">')
    o.append('<link rel="canonical" href="%s%s/%s">'
             % (BASE, lang, fichier(cle, lang)))
    for lg in LANGUES:
        o.append('<link rel="alternate" hreflang="%s" href="%s%s/%s">'
                 % (HTML_LANG[lg], BASE, lg, fichier(cle, lg)))
    o.append('<link rel="alternate" hreflang="x-default" href="%sfr/%s">'
             % (BASE, fichier(cle, "fr")))
    o.append('<link rel="icon" href="../assets/favicon.svg" '
             'type="image/svg+xml">')
    o.append('<link rel="stylesheet" href="../assets/site.css?v=%d">'
             % VERSION_CSS)
    o.append('<meta property="og:title" content="%s">' % ech(ttl_complet))
    o.append('<meta property="og:description" content="%s">' % ech(desc))
    o.append('<meta property="og:type" content="website">')
    o.append('<meta property="og:locale" content="%s">'
             % HTML_LANG[lang].replace("-", "_"))
    if cle == "accueil":
        o.append(donnees_structurees(lang, prefixe))
    o.append("</head>")
    # Le numéro vit dans le HTML, pas dans le script : un numéro dupliqué
    # dans un fichier .js finit un jour par diverger de celui des pages.
    o.append('<body class="p-%s" data-tel="%s">' % (cle, C.TEL_AFFICHE))
    o.append(entete(cle, lang, prefixe))
    o.append('<main id="principal" tabindex="-1">')
    if cle != "accueil":
        o.append('<div class="dans">%s</div>' % fil(cle, lang))
    o.append(corps)
    o.append("</main>")
    o.append(pied(cle, lang, prefixe))
    o.append('<script src="../assets/site.js?v=%d" defer></script>'
             % VERSION_CSS)
    o.append("</body></html>")
    del autre
    return "\n".join(o)


def aiguillage():
    """Racine : le cahier des charges impose /fr/ et /en/, donc la racine ne
    contient aucune page — seulement le renvoi vers la version française,
    qui est la langue de base."""
    o = ["<!doctype html>", '<html lang="fr-CA">', "<head>",
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,'
         'initial-scale=1">',
         '<meta http-equiv="refresh" content="0; url=fr/">',
         '<meta name="robots" content="noindex,nofollow">',
         "<title>%s — %s</title>" % (C.MARQUE, C.BASELINE[0]),
         '<link rel="canonical" href="%sfr/index.html">' % BASE,
         '<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">',
         '<link rel="stylesheet" href="assets/site.css?v=%d">' % VERSION_CSS,
         "</head>",
         '<body class="p-aiguillage"><main id="principal" class="dans">',
         '<img src="assets/marque-or.svg" alt="" width="72" height="89" '
         'aria-hidden="true">',
         "<h1>%s</h1>" % C.MARQUE,
         '<p><a href="fr/index.html">Continuer en français</a></p>',
         '<p><a href="en/index.html">Continue in English</a></p>',
         "</main></body></html>"]
    return "\n".join(o)


def plan_du_site():
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
         'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in C.PAGES:
        for lg in LANGUES:
            o.append("<url><loc>%s%s/%s</loc>" % (BASE, lg,
                                                  fichier(p[0], lg)))
            for lg2 in LANGUES:
                o.append('<xhtml:link rel="alternate" hreflang="%s" '
                         'href="%s%s/%s"/>'
                         % (HTML_LANG[lg2], BASE, lg2, fichier(p[0], lg2)))
            o.append("</url>")
    o.append("</urlset>")
    return "\n".join(o)


def robots():
    if DEMO:
        # Démo : rien ne doit être indexé. Le fichier le dit, et chaque page
        # porte en plus sa balise noindex — les deux, parce qu'un robots.txt
        # n'empêche pas l'indexation d'une URL déjà connue.
        return "User-agent: *\nDisallow: /\n"
    return "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE


def main():
    n = 0
    for lang in LANGUES:
        dossier = os.path.join(RACINE, lang)
        if not os.path.isdir(dossier):
            os.makedirs(dossier)
        for p in C.PAGES:
            html = gabarit(p[0], lang)
            chemin = os.path.join(dossier, fichier(p[0], lang))
            with open(chemin, "w", encoding="utf-8") as f:
                f.write(html + "\n")
            n += 1
    with open(os.path.join(RACINE, "index.html"), "w",
              encoding="utf-8") as f:
        f.write(aiguillage() + "\n")
    with open(os.path.join(RACINE, "sitemap.xml"), "w",
              encoding="utf-8") as f:
        f.write(plan_du_site() + "\n")
    with open(os.path.join(RACINE, "robots.txt"), "w",
              encoding="utf-8") as f:
        f.write(robots())
    print("%d pages + aiguillage + sitemap + robots  (DEMO=%s)"
          % (n, DEMO))


if __name__ == "__main__":
    main()
