# -*- coding: utf-8 -*-
"""
Ornements du site Master Skanda.

Tout ce qui est dessiné ici sort d'une seule géométrie, comme le blason
Adjaoudi : les variantes ne peuvent donc pas diverger entre elles.

Le registre visuel est moghol — arc en accolade, étoile à huit branches
(khatam), claustra (jali), marbre et or. C'est la palette demandée à
l'article 7.3 du cahier des charges du client : indigo profond, violet
minéral, or doux, ivoire.

Aucun nom de personne réelle n'apparaît nulle part, ni ici ni sur le site.
L'inspiration est dans le dessin ; elle n'a pas à être écrite.
"""

import math
import os

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
ACTIFS = os.path.join(RACINE, "assets")

# ---------------------------------------------------------------- palette
# Chaque valeur a été mesurée avant d'être écrite ici (voir README, section
# « Contrastes mesurés »). L'or n'est JAMAIS du texte sur fond clair : il
# tombe à 2,18:1 sur l'ivoire. C'est OR_TEXTE qui sert dans ce cas.
IVOIRE = "#F7F3EA"
MARBRE = "#FFFFFF"
INDIGO = "#1B1B3A"
NUIT = "#12122A"
VIOLET = "#4A3B6B"
OR = "#C9A227"
OR_CLAIR = "#D8B650"
OR_TEXTE = "#7E5C12"
ENCRE = "#23202B"

# ---------------------------------------------------------------- géométrie
LARGEUR = 200.0
HAUTEUR = 248.0
CX = LARGEUR / 2.0

ARC_DEMI = 67.0      # demi-largeur de l'arc
ARC_BAS = 212.0      # ligne de sol
ARC_RESSAUT = 140.0  # naissance de la courbe (springline)
ARC_SOMMET = 56.0    # pointe de l'accolade

ETOILE_CY = 148.0
ETOILE_R = 34.0


def _f(v):
    """3 décimales max, sans zéros inutiles : les SVG restent lisibles."""
    s = "%.3f" % v
    s = s.rstrip("0").rstrip(".")
    return s if s not in ("", "-0") else "0"


def arc_accolade(cx=CX, demi=ARC_DEMI, bas=ARC_BAS, ressaut=ARC_RESSAUT,
                 sommet=ARC_SOMMET, ferme=True):
    """Arc en accolade (ogee) — la courbe change de sens à mi-hauteur.

    C'est ce renversement qui distingue l'arc moghol de l'ogive gothique ;
    un arc simplement pointu lirait comme une chapelle, et un arc dont les
    deux moitiés courbent dans le même sens lit comme une cloche.

    La construction est explicite : un point d'inflexion I, une direction de
    tangente en I, et deux cubiques qui s'y raccordent avec la MÊME tangente.
    C'est la seule façon d'obtenir une accolade lisse ; en posant les points
    de contrôle à l'œil on obtient un bulbe.
    """
    h = float(ressaut - sommet)
    # point d'inflexion : à 55 % de la demi-largeur, à 42 % de la hauteur
    ix, iy = cx - 0.55 * demi, sommet + 0.42 * h
    # tangente en I, normalisée, orientée vers le haut et vers l'intérieur
    tx, ty = 0.46, -0.89
    n = math.hypot(tx, ty)
    tx, ty = tx / n, ty / n
    # longueurs de poignée proportionnelles à chaque corde
    c1 = math.hypot(ix - (cx - demi), iy - ressaut)
    c2 = math.hypot(cx - ix, sommet - iy)
    p = ["M %s %s" % (_f(cx - demi), _f(bas)),
         "L %s %s" % (_f(cx - demi), _f(ressaut))]

    def cub(x1, y1, x2, y2, x3, y3):
        return "C %s %s %s %s %s %s" % (_f(x1), _f(y1), _f(x2), _f(y2),
                                        _f(x3), _f(y3))

    # bas de l'accolade : part vertical, bombe vers l'extérieur
    p.append(cub(cx - demi, ressaut - 0.55 * c1,
                 ix - 0.46 * c1 * tx, iy - 0.46 * c1 * ty,
                 ix, iy))
    # haut de l'accolade : repart dans l'autre sens, finit en pointe
    p.append(cub(ix + 0.44 * c2 * tx, iy + 0.44 * c2 * ty,
                 cx - 0.13 * demi, sommet + 0.30 * h,
                 cx, sommet))
    # miroir
    p.append(cub(cx + 0.13 * demi, sommet + 0.30 * h,
                 (2 * cx - ix) - 0.44 * c2 * tx, iy + 0.44 * c2 * ty,
                 2 * cx - ix, iy))
    p.append(cub((2 * cx - ix) + 0.46 * c1 * tx, iy - 0.46 * c1 * ty,
                 cx + demi, ressaut - 0.55 * c1,
                 cx + demi, ressaut))
    p.append("L %s %s" % (_f(cx + demi), _f(bas)))
    if ferme:
        p.append("Z")
    return " ".join(p)


def khatam(cx=CX, cy=ETOILE_CY, r=ETOILE_R, tour=22.5):
    """Étoile à huit branches : l'intersection de deux carrés superposés.

    Le rayon intérieur n'est pas choisi à l'œil — c'est cos(45°)/cos(22,5°),
    la valeur qui fait que les côtés des deux carrés sont bien alignés.
    """
    interne = r * math.cos(math.radians(45.0)) / math.cos(math.radians(22.5))
    pts = []
    for i in range(8):
        a = math.radians(tour + i * 45.0)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        b = math.radians(tour + i * 45.0 + 22.5)
        pts.append((cx + interne * math.cos(b), cy + interne * math.sin(b)))
    d = "M " + " L ".join("%s %s" % (_f(x), _f(y)) for x, y in pts) + " Z"
    return d


def fleuron(cx=CX, base=ARC_SOMMET, haut=42.0, larg=17.0):
    """Fleuron : le bouton de lotus qui prolonge la pointe de l'arc.

    Il pousse DANS l'axe de la pointe, il n'est pas posé au-dessus — un
    dôme flottant au-dessus d'un arc se lit comme un objet séparé, ce que
    la première version faisait.
    """
    b = base + 3.0
    bulbe = ("M %s %s C %s %s %s %s %s %s C %s %s %s %s %s %s Z" % (
        _f(cx), _f(b),
        _f(cx - larg * 0.50), _f(b - haut * 0.10),
        _f(cx - larg), _f(b - haut * 0.42),
        _f(cx), _f(b - haut * 0.74),
        _f(cx + larg), _f(b - haut * 0.42),
        _f(cx + larg * 0.50), _f(b - haut * 0.10),
        _f(cx), _f(b)))
    tige = "M %s %s L %s %s" % (_f(cx), _f(b - haut * 0.74),
                                _f(cx), _f(b - haut * 0.96))
    perle = (cx, b - haut * 1.06, 4.6)
    return bulbe, tige, perle


def _entete(largeur, hauteur, titre):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" '
            'width="%s" height="%s" role="img" aria-label="%s">'
            % (_f(largeur), _f(hauteur), _f(largeur), _f(hauteur), titre))


def marque(teinte=OR, fond=None, titre="Marque Master Skanda"):
    """La marque : arc en accolade, khatam au centre, dôme au sommet.

    `teinte` sert pour tous les traits — la marque est monochrome par
    construction, donc elle survit à une impression une couleur, à un fax,
    à une broderie et à un favicon de 16 pixels.
    """
    vide = fond if fond else "#FFFFFF"
    o = [_entete(LARGEUR, HAUTEUR, titre)]
    if fond:
        o.append('<rect width="%s" height="%s" fill="%s"/>'
                 % (_f(LARGEUR), _f(HAUTEUR), fond))
    # Le niche est une SURFACE, pas un contour. Un arc en fil de fer se lit
    # comme une cage à oiseaux dès qu'on descend sous 60 px de large ; une
    # surface pleine tient jusqu'au favicon.
    o.append('<g fill="%s">' % teinte)
    o.append('<path d="%s"/>' % arc_accolade())
    bulbe, tige, perle = fleuron()
    o.append('<path d="%s"/>' % bulbe)
    o.append('<path d="%s" stroke="%s" stroke-width="3.4" '
             'stroke-linecap="round"/>' % (tige, teinte))
    o.append('<circle cx="%s" cy="%s" r="%s"/>'
             % (_f(perle[0]), _f(perle[1]), _f(perle[2])))
    o.append('<rect x="%s" y="%s" width="%s" height="5.4" rx="2.7"/>'
             % (_f(CX - ARC_DEMI - 17), _f(ARC_BAS), _f(2 * ARC_DEMI + 34)))
    o.append('<rect x="%s" y="%s" width="%s" height="2.6" rx="1.3"/>'
             % (_f(CX - ARC_DEMI - 28), _f(ARC_BAS + 11),
                _f(2 * ARC_DEMI + 56)))
    o.append("</g>")
    # khatam évidé dans la niche, avec une contre-étoile pleine au cœur
    o.append('<path d="%s" fill="%s"/>' % (khatam(), vide))
    o.append('<path d="%s" fill="%s"/>'
             % (khatam(r=ETOILE_R * 0.46), teinte))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
             % (_f(CX), _f(ETOILE_CY), _f(ETOILE_R * 0.13), vide))
    o.append("</svg>")
    return "\n".join(o)


def favicon():
    """16 px : l'arc et le dôme disparaissent, seul le khatam reste lisible."""
    o = [_entete(64, 64, "Master Skanda")]
    o.append('<rect width="64" height="64" rx="10" fill="%s"/>' % INDIGO)
    o.append('<path d="%s" fill="%s"/>' % (khatam(cx=32, cy=32, r=21), OR_CLAIR))
    o.append('<path d="%s" fill="%s"/>'
             % (khatam(cx=32, cy=32, r=21 * 0.52), INDIGO))
    o.append('<circle cx="32" cy="32" r="3.4" fill="%s"/>' % OR_CLAIR)
    o.append("</svg>")
    return "\n".join(o)


def jali(tuile=120.0, teinte=OR, epaisseur=1.5):
    """Claustra : la tuile qui se répète en fond, très faiblement opaque.

    Cercles aux quatre coins plus un au centre — les arcs qui se croisent
    dessinent la résille. Le motif est aligné sur la tuile, donc il se
    raccorde exactement quand `background-repeat` le répète.
    """
    r = tuile * 0.5
    o = [_entete(tuile, tuile, "Claustra")]
    o.append('<g fill="none" stroke="%s" stroke-width="%s" opacity="1">'
             % (teinte, _f(epaisseur)))
    for cx, cy in ((0, 0), (tuile, 0), (0, tuile), (tuile, tuile),
                   (r, r)):
        o.append('<circle cx="%s" cy="%s" r="%s"/>' % (_f(cx), _f(cy), _f(r)))
    # Une étoile au centre seulement. Aux quatre coins elle serait coupée par
    # le bord de la tuile et se lirait comme quatre crochets cassés — c'est
    # ce que faisait la première version.
    o.append('<path d="%s"/>' % khatam(cx=r, cy=r, r=tuile * 0.15))
    o.append("</g></svg>")
    return "\n".join(o)


def frise(largeur=1200.0, hauteur=26.0, teinte=OR, pas=52.0):
    """Séparateur de section : chaîne de losanges et de perles.

    Purement décoratif — d'où `aria-hidden` partout où il est posé, et d'où
    le fait que son contraste de 2,18:1 sur l'ivoire ne pose pas de
    problème : il ne porte aucune information.
    """
    cy = hauteur / 2.0
    o = [_entete(largeur, hauteur, "Frise")]
    o.append('<g stroke="%s" fill="none" stroke-width="1.4">' % teinte)
    o.append('<path d="M 0 %s L %s %s"/>' % (_f(cy), _f(largeur), _f(cy)))
    o.append("</g>")
    o.append('<g fill="%s">' % teinte)
    x = pas / 2.0
    n = 0
    while x < largeur:
        if n % 2 == 0:
            d = 6.4
            o.append('<path d="M %s %s L %s %s L %s %s L %s %s Z"/>'
                     % (_f(x), _f(cy - d), _f(x + d), _f(cy),
                        _f(x), _f(cy + d), _f(x - d), _f(cy)))
        else:
            o.append('<circle cx="%s" cy="%s" r="2.6"/>' % (_f(x), _f(cy)))
        x += pas / 2.0
        n += 1
    o.append("</g></svg>")
    return "\n".join(o)


def fenetre(largeur=420.0, hauteur=520.0, teinte=OR, fond=INDIGO):
    """Panneau ornemental — la « fenêtre » qui remplace une photographie.

    Aucune photographie du praticien ni du cabinet n'a été fournie, et
    l'article 7.3 du cahier des charges interdit d'en générer une. Donc à
    chaque emplacement prévu pour une image, c'est ce panneau qui est posé,
    avec sous lui la phrase qui dit ce qu'on attend.
    """
    cx = largeur / 2.0
    demi = largeur * 0.34
    bas = hauteur * 0.86
    ressaut = hauteur * 0.52
    sommet = hauteur * 0.12
    o = [_entete(largeur, hauteur, "Panneau ornemental")]
    o.append('<rect width="%s" height="%s" fill="%s"/>'
             % (_f(largeur), _f(hauteur), fond))
    o.append('<defs><clipPath id="cl"><path d="%s"/></clipPath></defs>'
             % arc_accolade(cx=cx, demi=demi, bas=bas, ressaut=ressaut,
                            sommet=sommet))
    o.append('<g clip-path="url(#cl)" opacity="0.34">')
    t = 46.0
    y = 0.0
    while y < hauteur + t:
        x = -t
        while x < largeur + t:
            o.append('<circle cx="%s" cy="%s" r="%s" fill="none" '
                     'stroke="%s" stroke-width="1"/>'
                     % (_f(x), _f(y), _f(t / 2.0), teinte))
            x += t
        y += t
    o.append("</g>")
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="3"/>'
             % (arc_accolade(cx=cx, demi=demi, bas=bas, ressaut=ressaut,
                             sommet=sommet), teinte))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.2"/>'
             % (arc_accolade(cx=cx, demi=demi - 11, bas=bas - 4,
                             ressaut=ressaut - 6, sommet=sommet + 13),
                teinte))
    # centre optique de la niche, pas milieu arithmétique de la hauteur
    o.append('<path d="%s" fill="%s"/>'
             % (khatam(cx=cx, cy=sommet + (bas - sommet) * 0.52,
                       r=largeur * 0.095), teinte))
    o.append('<path d="%s" fill="%s"/>'
             % (khatam(cx=cx, cy=sommet + (bas - sommet) * 0.52,
                       r=largeur * 0.095 * 0.46), fond))
    o.append('<path d="M %s %s L %s %s" stroke="%s" stroke-width="2.4"/>'
             % (_f(cx - demi - 20), _f(bas), _f(cx + demi + 20), _f(bas),
                teinte))
    o.append("</svg>")
    return "\n".join(o)


def ecrire():
    if not os.path.isdir(ACTIFS):
        os.makedirs(ACTIFS)
    fichiers = {
        "marque-or.svg": marque(OR),
        "marque-or-clair.svg": marque(OR_CLAIR),
        "marque-indigo.svg": marque(INDIGO),
        "marque-ivoire.svg": marque(IVOIRE),
        "favicon.svg": favicon(),
        "jali.svg": jali(),
        "frise.svg": frise(),
        "fenetre.svg": fenetre(),
    }
    for nom, contenu in sorted(fichiers.items()):
        with open(os.path.join(ACTIFS, nom), "w", encoding="utf-8") as f:
            f.write(contenu + "\n")
        print("ecrit  assets/%s  (%d o)" % (nom, len(contenu) + 1))
    return len(fichiers)


if __name__ == "__main__":
    n = ecrire()
    print("%d fichiers d'ornement" % n)
