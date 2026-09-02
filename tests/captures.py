# -*- coding: utf-8 -*-
"""
Aperçus du site, écrits dans apercus/.

Contrainte dure : aucune image ne dépasse 2000 px dans un sens. On ne
photographie donc jamais la page entière — on fixe la fenêtre, on fait
défiler, et on assemble si besoin.

    python3 tests/captures.py [http://127.0.0.1:8873/]
"""

import os
import sys

from playwright.sync_api import sync_playwright
from PIL import Image

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI)
SORTIE = os.path.join(RACINE, "apercus")

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8873/"
if not BASE.endswith("/"):
    BASE += "/"

# (nom, page, largeur, hauteur, défilement)
VUES = [
    ("ms-01-accueil",          "fr/index.html", 1280, 800, 0),
    ("ms-02-cabinet",          "fr/index.html", 1280, 800, 790),
    ("ms-03-consultations",    "fr/index.html", 1280, 800, 1420),
    ("ms-04-cadre",            "fr/index.html", 1280, 800, 2200),
    ("ms-05-services",         "fr/services.html", 1280, 800, 190),
    ("ms-06-service-affaires", "fr/guidance-affaires.html", 1280, 800, 220),
    ("ms-07-attente-service",  "fr/guidance-affaires.html", 1280, 800, 1080),
    ("ms-08-apropos",          "fr/a-propos.html", 1280, 800, 210),
    ("ms-09-apropos-manque",   "fr/a-propos.html", 1280, 800, 900),
    ("ms-10-approche",         "fr/approche-et-ethique.html", 1280, 800, 200),
    ("ms-11-nest-pas",         "fr/approche-et-ethique.html", 1280, 800, 760),
    ("ms-12-faq",              "fr/questions-frequentes.html", 1280, 800, 190),
    ("ms-13-rendez-vous",      "fr/prendre-rendez-vous.html", 1280, 800, 300),
    ("ms-14-avis",             "fr/avis.html", 1280, 800, 150),
    ("ms-15-contact",          "fr/contact-et-itineraire.html", 1280, 800,
     180),
    ("ms-16-confidentialite",  "fr/confidentialite.html", 1280, 800, 230),
    ("ms-17-accessibilite",    "fr/accessibilite.html", 1280, 800, 210),
    ("ms-18-mobile-accueil",   "fr/index.html", 390, 780, 0),
    ("ms-19-mobile-cartes",    "fr/index.html", 390, 780, 1150),
    ("ms-20-mobile-attente",   "fr/a-propos.html", 390, 780, 1250),
    ("ms-21-mobile-formulaire", "fr/prendre-rendez-vous.html", 390, 780, 620),
    ("ms-22-anglais-accueil",  "en/index.html", 1280, 800, 0),
    ("ms-23-anglais-approche", "en/approach-and-ethics.html", 1280, 800, 200),
    ("ms-24-320",              "fr/services.html", 320, 720, 240),
]


def capture():
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for nom, rel, w, h, sc in VUES:
            pg = nav.new_page(viewport={"width": w, "height": h})
            pg.goto(BASE + rel, wait_until="networkidle")
            pg.wait_for_timeout(300)
            if sc:
                pg.evaluate("window.scrollTo(0,%d)" % sc)
                pg.wait_for_timeout(260)
            chemin = os.path.join(SORTIE, nom + ".png")
            pg.screenshot(path=chemin)
            pg.close()
            im = Image.open(chemin)
            assert im.width <= 2000 and im.height <= 2000, \
                "%s fait %dx%d" % (nom, im.width, im.height)
            print("%-26s %dx%d" % (nom, im.width, im.height))
        nav.close()


def planche_de_marque():
    """Une planche des variantes, rendue depuis les SVG maîtres — jamais
    redessinée à la main, sinon la planche et les fichiers divergent."""
    import cairosvg
    A = os.path.join(RACINE, "assets")
    pieces = [("marque-or.svg", "#F7F3EA", 190),
              ("marque-ivoire.svg", "#1B1B3A", 190),
              ("marque-indigo.svg", "#F7F3EA", 190),
              ("favicon.svg", None, 96)]
    imgs = []
    for nom, fond, larg in pieces:
        tmp = os.path.join(SORTIE, "_" + nom + ".png")
        cairosvg.svg2png(url=os.path.join(A, nom), write_to=tmp,
                         background_color=fond, output_width=larg)
        imgs.append(Image.open(tmp).convert("RGB"))
    marge = 40
    W = sum(i.width for i in imgs) + marge * (len(imgs) + 1)
    H = max(i.height for i in imgs) + marge * 2
    planche = Image.new("RGB", (W, H), "#EFEAE0")
    x = marge
    for i in imgs:
        planche.paste(i, (x, (H - i.height) // 2))
        x += i.width + marge
    chemin = os.path.join(SORTIE, "ms-00-marque.png")
    planche.save(chemin)
    for nom, _, _ in pieces:
        os.remove(os.path.join(SORTIE, "_" + nom + ".png"))
    print("%-26s %dx%d" % ("ms-00-marque", planche.width, planche.height))


if __name__ == "__main__":
    planche_de_marque()
    capture()
