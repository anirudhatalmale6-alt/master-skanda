# -*- coding: utf-8 -*-
"""
Tout le texte du site, en couples (français, anglais).

RÈGLE DE PRODUCTION — un seul principe gouverne ce fichier.

    Ne peut être affirmé sur le site que ce qui vient soit de la fiche
    Google publique, soit du cahier des charges du client. Tout le reste
    sort en « À confirmer », avec la condition écrite à côté.

Les faits sourcés sont exactement ceux-ci, et il n'y en a pas d'autres :
nom affiché, catégorie, adresse, proximité du métro Côte-Vertu, numéro de
téléphone, et le fait que la communication récente du propriétaire porte
sur les enjeux d'affaires, la croissance, les finances, les partenariats
et la carrière.

Ne figurent donc nulle part : tarif, durée, horaires, années d'expérience,
biographie, certification, langue parlée par le praticien, note, nombre
d'avis, témoignage, photographie.

Interdits par le cahier des charges lui-même (articles 3.2, 7.1 et 10.3),
et interdits ici : promesse de résultat, garantie, guérison, gain, conseil
médical, juridique ou financier, superlatif invérifiable, urgence
artificielle, peur.
"""

# ------------------------------------------------------------------ marque
MARQUE = "Master Skanda"
# Le nom complet tel qu'il figure sur la fiche. Il n'est employé qu'aux
# endroits où c'est l'identification de l'établissement qui compte.
NOM_FICHE = "Psychic & Spiritual Healer Master Skanda"
BASELINE = ("Guidance spirituelle et astrologique",
            "Psychic and spiritual guidance")

# ------------------------------------------------------------------- fiche
ADRESSE = ("1485, rue MacDonald, Saint-Laurent (Québec) H4L 2A8",
           "1485 MacDonald Street, Saint-Laurent, Quebec H4L 2A8")
RUE = ("1485, rue MacDonald", "1485 MacDonald Street")
VILLE = ("Saint-Laurent (Québec) H4L 2A8", "Saint-Laurent, Quebec H4L 2A8")
METRO = ("Près du métro Côte-Vertu", "Near Côte-Vertu metro station")
TEL_AFFICHE = "+1 514 895-1119"
TEL_LIEN = "+15148951119"
LIEN_FICHE = "https://maps.app.goo.gl/24SxSGCk8UKfnD9b8"

# -------------------------------------------------- vocabulaire de l'attente
# Ce site a SON mot, et il ne se mêle pas à ceux des autres chantiers
# (« à vérifier » chez Amarimmo, « à définir » chez EdenFlor, « To be
# decided » chez Equilibrium, « En attente d'autorisation » à la
# Seigneurie). Ici c'est le mot du cahier des charges du client lui-même.
ATTENTE = ("À confirmer", "To be confirmed")

# ------------------------------------------------------------------ mentions
# Article 10.3 du cahier des charges, repris mot pour mot en français.
PRUDENCE = (
    "Les consultations offrent une perspective spirituelle ou astrologique "
    "à des fins de réflexion personnelle. Les résultats ne peuvent être "
    "garantis. Elles ne remplacent pas les services d'un professionnel de "
    "la santé, du droit, de la finance ou de la sécurité publique. En "
    "situation d'urgence, contactez les services compétents.",
    "Consultations offer a spiritual or astrological perspective for "
    "personal reflection. Results cannot be guaranteed. They do not replace "
    "the services of a health, legal, financial or public safety "
    "professional. In an emergency, contact the appropriate services.")

MAJEURS = ("Service réservé aux personnes majeures.",
           "Adults only.")

# ------------------------------------------------------------------- pages
# (clé, fichier fr, fichier en, titre fr, titre en, dans le menu)
PAGES = [
    ("accueil", "index.html", "index.html",
     "Accueil", "Home", False),
    ("services", "services.html", "services.html",
     "Services", "Services", True),
    ("svc-affaires", "guidance-affaires.html", "business-guidance.html",
     "Enjeux d'affaires", "Business matters", False),
    ("svc-carriere", "croissance-carriere.html", "growth-and-career.html",
     "Croissance et carrière", "Growth and career", False),
    ("svc-finances", "preoccupations-financieres.html",
     "financial-concerns.html",
     "Préoccupations financières", "Financial concerns", False),
    ("svc-partenariats", "partenariats.html", "partnerships.html",
     "Partenariats", "Partnerships", False),
    ("apropos", "a-propos.html", "about.html",
     "À propos", "About", True),
    ("approche", "approche-et-ethique.html", "approach-and-ethics.html",
     "Approche et éthique", "Approach and ethics", True),
    ("faq", "questions-frequentes.html", "faq.html",
     "Questions fréquentes", "Frequently asked questions", True),
    ("reserver", "prendre-rendez-vous.html", "book-an-appointment.html",
     "Prendre rendez-vous", "Book an appointment", True),
    ("contact", "contact-et-itineraire.html", "contact-and-directions.html",
     "Contact et itinéraire", "Contact and directions", True),
    ("avis", "avis.html", "reviews.html",
     "Avis", "Reviews", False),
    ("confidentialite", "confidentialite.html", "privacy.html",
     "Politique de confidentialité", "Privacy policy", False),
    ("conditions", "conditions.html", "terms.html",
     "Conditions de service", "Terms of service", False),
    ("accessibilite", "accessibilite.html", "accessibility.html",
     "Accessibilité", "Accessibility", False),
]

MENU_CTA = ("Prendre rendez-vous", "Book an appointment")
# Version courte pour la barre d'actions mobile, où « Prendre rendez-vous »
# passait sur deux lignes dans un bouton de 48 px de haut.
MENU_CTA_COURT = ("Rendez-vous", "Book")
APPELER = ("Appeler", "Call")

# Le cahier des charges demande un « menu court » (F-01). Les titres de
# page complets, eux, restent longs parce qu'ils servent aussi de titre de
# document et de fil d'Ariane — d'où deux libellés distincts.
MENU_COURT = {
    "services": ("Services", "Services"),
    "apropos": ("À propos", "About"),
    "approche": ("Approche", "Approach"),
    "faq": ("Questions", "FAQ"),
    "contact": ("Contact", "Contact"),
}

# ------------------------------------------------------------------ accueil
ACC_TITRE = ("Guidance spirituelle et astrologique à Saint-Laurent",
             "Spiritual and astrological guidance in Saint-Laurent")
ACC_SOUS = ("Un espace confidentiel pour réfléchir à vos choix personnels "
            "et professionnels.",
            "A confidential space to think through your personal and "
            "professional choices.")

ACC_INTRO = [
    ("Master Skanda reçoit au 1485, rue MacDonald, à Saint-Laurent, près du "
     "métro Côte-Vertu.",
     "Master Skanda receives clients at 1485 MacDonald Street in "
     "Saint-Laurent, near Côte-Vertu metro station."),
    ("Les consultations portent sur les décisions qu'on hésite à prendre "
     "seul : une orientation professionnelle, une croissance à préparer, "
     "une question financière qui revient, un partenariat à évaluer.",
     "Consultations deal with the decisions people hesitate to take alone: "
     "a professional direction, growth to prepare for, a financial question "
     "that keeps coming back, a partnership to weigh up."),
    ("Le cadre est posé d'avance : un entretien confidentiel, une "
     "perspective spirituelle et astrologique, aucun résultat promis, et "
     "rien qui vous engage au-delà de la rencontre.",
     "The framework is set in advance: a confidential conversation, a "
     "spiritual and astrological perspective, no promised outcome, and "
     "nothing that commits you beyond the meeting itself."),
]

ACC_PILIERS = [
    ("Confidentiel",
     "Ce qui se dit pendant la consultation reste dans la pièce. Le site ne "
     "vous demande jamais de raconter votre situation par écrit.",
     "Confidential",
     "What is said during a consultation stays in the room. This site never "
     "asks you to write your situation down."),
    ("Sans promesse",
     "Aucune garantie de résultat, aucun retour assuré, aucune pression. "
     "Une consultation est un éclairage, pas une solution.",
     "No promises",
     "No guaranteed outcome, no assured return, no pressure. A consultation "
     "is a perspective, not a solution."),
    ("Sur place, près du métro",
     "Le cabinet est à Saint-Laurent, près du métro Côte-Vertu. L'adresse "
     "exacte et l'itinéraire sont sur la page Contact.",
     "In person, near the metro",
     "The practice is in Saint-Laurent, near Côte-Vertu metro station. The "
     "exact address and directions are on the Contact page."),
]

# ----------------------------------------------------------------- services
SERVICES_INTRO = (
    "Quatre consultations sont proposées au lancement. Elles reprennent les "
    "sujets sur lesquels porte la communication récente du propriétaire : "
    "les enjeux d'affaires, la croissance et la carrière, les préoccupations "
    "financières et les partenariats.",
    "Four consultations are offered at launch. They follow the subjects the "
    "owner's recent communication covers: business matters, growth and "
    "career, financial concerns and partnerships.")

SERVICES_NOTE = (
    "Le catalogue reste provisoire tant que le propriétaire n'a pas arrêté "
    "la liste exacte, les durées, les formats et les tarifs.",
    "The catalogue remains provisional until the owner has settled the exact "
    "list, durations, formats and prices.")

# clé -> (titre, résumé, [situations], [ce que ça apporte], [ce que ça ne
#         remplace pas]) en français puis en anglais
SERVICES = {
    "svc-affaires": {
        "resume": (
            "Une consultation pour poser à plat une décision d'affaires et "
            "regarder ce qui pèse dans la balance.",
            "A consultation to lay out a business decision and look at what "
            "actually weighs on it."),
        "situations": [
            ("Une décision qui traîne depuis des semaines et qu'on retourne "
             "sans trancher.",
             "A decision that has dragged on for weeks without being made."),
            ("Un choix entre deux directions qui semblent aussi "
             "défendables l'une que l'autre.",
             "A choice between two directions that seem equally "
             "defensible."),
            ("Le besoin de parler d'un sujet professionnel à quelqu'un "
             "d'extérieur à l'entreprise.",
             "The need to talk a professional matter over with someone "
             "outside the business."),
        ],
        "apporte": [
            ("Un temps de recul, hors du bruit habituel de la décision.",
             "Time to step back, away from the usual noise of the "
             "decision."),
            ("Une lecture symbolique de la situation, formulée simplement.",
             "A symbolic reading of the situation, put in plain words."),
            ("Des questions que personne d'autre ne vous a posées.",
             "Questions no one else has asked you."),
        ],
        "pas": [
            ("Un avis juridique, comptable ou fiscal.",
             "Legal, accounting or tax advice."),
            ("Une étude de marché ou un plan d'affaires.",
             "A market study or a business plan."),
            ("Une garantie sur l'issue de la décision.",
             "Any guarantee about how the decision turns out."),
        ],
    },
    "svc-carriere": {
        "resume": (
            "Une consultation autour d'une transition professionnelle, "
            "d'une progression ou d'un changement de cap.",
            "A consultation around a professional transition, a step "
            "forward, or a change of direction."),
        "situations": [
            ("Un poste qui ne correspond plus, sans que la suite soit "
             "claire.",
             "A role that no longer fits, with no clear next step."),
            ("Une offre à accepter ou à refuser, avec peu de temps devant "
             "soi.",
             "An offer to accept or turn down, with little time to think."),
            ("Un projet personnel qu'on n'ose pas encore commencer.",
             "A personal project one does not yet dare to start."),
        ],
        "apporte": [
            ("Une mise en mots de ce qui bloque, avant même d'y répondre.",
             "Putting into words what is blocking, before answering it."),
            ("Un éclairage sur le moment plutôt que sur la seule décision.",
             "A perspective on the timing, not only on the decision."),
            ("Un espace pour dire ce qu'on ne dit pas au travail.",
             "A space to say what is not said at work."),
        ],
        "pas": [
            ("Un service d'orientation professionnelle certifié.",
             "A certified career-guidance service."),
            ("Un accompagnement psychologique ou thérapeutique.",
             "Psychological or therapeutic support."),
            ("Une promesse d'embauche, de promotion ou de revenu.",
             "Any promise of hiring, promotion or income."),
        ],
    },
    "svc-finances": {
        "resume": (
            "Une réflexion astrologique autour d'une préoccupation "
            "financière. Ce n'est pas du conseil financier, et ça ne peut "
            "pas en tenir lieu.",
            "An astrological reflection around a financial concern. This is "
            "not financial advice and cannot take its place."),
        "situations": [
            ("Une inquiétude d'argent qui revient et qu'on n'arrive pas à "
             "poser.",
             "A money worry that keeps returning and cannot be set down."),
            ("Un engagement financier qu'on hésite à prendre.",
             "A financial commitment one hesitates to take on."),
            ("Le sentiment de répéter le même schéma d'une année à "
             "l'autre.",
             "The sense of repeating the same pattern year after year."),
        ],
        "apporte": [
            ("Une occasion de nommer la préoccupation sans être jugé.",
             "A chance to name the concern without being judged."),
            ("Une lecture du cycle plutôt qu'un pronostic chiffré.",
             "A reading of the cycle rather than a numeric forecast."),
            ("Un cadre calme pour une question qui rend rarement calme.",
             "A calm setting for a question that rarely feels calm."),
        ],
        "pas": [
            ("Un conseil en placement, en crédit ou en assurance.",
             "Investment, credit or insurance advice."),
            ("Une prévision de gain, de perte ou de rendement.",
             "Any forecast of gain, loss or return."),
            ("Une recommandation d'engager ou de retirer de l'argent.",
             "Any recommendation to commit or withdraw money."),
        ],
    },
    "svc-partenariats": {
        "resume": (
            "Une consultation sur la dynamique d'un partenariat d'affaires : "
            "ce qui s'accorde, ce qui frotte, ce qui n'a pas été dit.",
            "A consultation on the dynamics of a business partnership: what "
            "fits, what rubs, what has not been said."),
        "situations": [
            ("Une association à conclure et un doute qui persiste.",
             "A partnership about to be signed, with a doubt that lingers."),
            ("Une relation d'affaires qui s'est tendue sans motif clair.",
             "A business relationship that has grown tense for no clear "
             "reason."),
            ("Deux façons de travailler qui ne se rencontrent plus.",
             "Two ways of working that no longer meet."),
        ],
        "apporte": [
            ("Une description de la dynamique, dite à voix haute.",
             "A description of the dynamic, said out loud."),
            ("Un regard sur les deux côtés, pas seulement sur le vôtre.",
             "A look at both sides, not only yours."),
            ("Un point de départ pour la conversation que vous devrez "
             "avoir.",
             "A starting point for the conversation you will have to have."),
        ],
        "pas": [
            ("Une médiation, un arbitrage ou une représentation.",
             "Mediation, arbitration or representation."),
            ("Un avis sur un contrat ou sur vos droits.",
             "An opinion on a contract or on your rights."),
            ("Une consultation sur une personne absente et non "
             "consentante.",
             "A consultation about an absent person who has not consented."),
        ],
    },
}

# Ce qui manque pour CHAQUE page de service, et ce qui débloque.
SERVICE_ATTENTES = [
    ("Durée de la consultation",
     "Le propriétaire doit fixer les durées (décision D-02).",
     "Length of the consultation",
     "The owner must set the durations (decision D-02)."),
    ("Formats offerts : sur place, téléphone, vidéo",
     "Décision D-03. Rien n'est affiché tant que ce n'est pas tranché, "
     "pour ne pas annoncer un service qui n'existe pas.",
     "Formats offered: in person, phone, video",
     "Decision D-03. Nothing is shown until this is settled, so that no "
     "service is announced that does not exist."),
    ("Tarif, taxes, dépôt, annulation et remboursement",
     "Décisions D-02 et D-05. Un prix affiché doit être exact avant "
     "confirmation, taxes comprises.",
     "Price, taxes, deposit, cancellation and refund",
     "Decisions D-02 and D-05. A displayed price must be accurate before "
     "confirmation, taxes included."),
    ("Langues dans lesquelles la consultation se déroule",
     "À ne pas confondre avec les langues du site. Le propriétaire doit "
     "indiquer les langues qu'il parle réellement.",
     "Languages the consultation is held in",
     "Not to be confused with the languages of this site. The owner must "
     "state the languages actually spoken."),
]

# ------------------------------------------------------------------ à propos
APROPOS_INTRO = (
    "Cette page est volontairement vide de tout ce qui n'a pas été fourni.",
    "This page is deliberately empty of everything that was not provided.")

APROPOS_TEXTE = [
    ("Une page « À propos » sert à répondre à une seule question : à qui "
     "vais-je parler ? Y répondre demande des éléments vérifiables — un "
     "parcours, un nombre d'années exact, des méthodes nommées, une "
     "photographie authentique, et pour chaque certification l'organisme "
     "qui l'a délivrée.",
     "An About page answers one question: who am I going to talk to? "
     "Answering it takes verifiable material — a background, an exact "
     "number of years, named methods, an authentic photograph, and for each "
     "certification the body that issued it."),
    ("Rien de tout cela n'a encore été transmis, et rien de tout cela ne "
     "s'invente. C'est aussi ce que demande l'article 4.3 du cahier des "
     "charges. La page est donc construite, mais ses contenus attendent.",
     "None of that has been provided yet, and none of it can be invented. "
     "That is also what section 4.3 of the specification requires. The page "
     "is therefore built, but its content is waiting."),
    ("Aucune image générée ne représentera le praticien, le cabinet ou des "
     "clients. Le panneau ci-contre est un ornement dessiné, pas une "
     "photographie retouchée : personne ne peut le prendre pour le lieu.",
     "No generated image will stand in for the practitioner, the practice "
     "or clients. The panel alongside is a drawn ornament, not a retouched "
     "photograph: no one can mistake it for the place."),
]

APROPOS_ATTENTES = [
    ("Nom professionnel principal",
     "La fiche porte « Master Skanda », une publication du propriétaire "
     "mentionne « Master Parasuram ». Un seul nom doit être retenu, avec "
     "mention d'un alias uniquement s'il est réel et assumé (décision "
     "D-01).",
     "Main professional name",
     "The listing reads “Master Skanda”, while a publication by the owner "
     "mentions “Master Parasuram”. One name must be chosen, with an alias "
     "mentioned only if it is real and acknowledged (decision D-01)."),
    ("Parcours et nombre d'années d'expérience",
     "Un chiffre exact, pas un ordre de grandeur.",
     "Background and exact number of years of experience",
     "An exact figure, not an approximation."),
    ("Méthodes pratiquées",
     "Nommées telles qu'elles sont réellement pratiquées.",
     "Methods practised",
     "Named as they are actually practised."),
    ("Certifications",
     "Chacune avec l'organisme émetteur. Une certification sans émetteur "
     "nommé n'est pas publiable.",
     "Certifications",
     "Each with its issuing body. A certification with no named issuer "
     "cannot be published."),
    ("Photographie authentique du praticien et du cabinet",
     "Avec l'auteur ou le détenteur des droits et l'étendue de "
     "l'autorisation.",
     "Authentic photograph of the practitioner and the practice",
     "With the author or rights holder and the extent of the "
     "authorisation."),
    ("Langues parlées",
     "Celles de la consultation, distinctes des langues du site.",
     "Languages spoken",
     "Those of the consultation, distinct from the languages of this site."),
]

# --------------------------------------------------------- approche, éthique
APPROCHE_INTRO = (
    "Ce que le cadre est, et ce qu'il n'est pas. Cette page est la plus "
    "importante du site.",
    "What the framework is, and what it is not. This is the most important "
    "page on the site.")

APPROCHE_EST = [
    ("Un entretien confidentiel",
     "Ce qui est dit pendant la consultation n'est pas partagé, pas publié "
     "et pas repris ailleurs.",
     "A confidential conversation",
     "What is said during a consultation is not shared, not published and "
     "not reused elsewhere."),
    ("Une perspective, offerte pour réfléchir",
     "Une lecture spirituelle et astrologique, proposée comme un éclairage "
     "parmi d'autres.",
     "A perspective, offered to think with",
     "A spiritual and astrological reading, offered as one light among "
     "others."),
    ("Un cadre expliqué avant d'entrer",
     "Durée, format, tarif et politique d'annulation sont dits avant la "
     "consultation, jamais découverts après.",
     "A framework explained before you enter",
     "Length, format, price and cancellation policy are stated before the "
     "consultation, never discovered afterwards."),
    ("Un accueil sans condition d'appartenance",
     "Aucune question sur l'origine, la religion, l'orientation ou la "
     "situation familiale n'est nécessaire pour prendre rendez-vous.",
     "A welcome with no membership condition",
     "No question about origin, religion, orientation or family situation "
     "is needed to book."),
]

APPROCHE_NEST_PAS = [
    ("Ce n'est pas un soin de santé",
     "Aucun diagnostic, aucun traitement, aucune recommandation "
     "d'interrompre un suivi médical ou une médication.",
     "It is not health care",
     "No diagnosis, no treatment, no recommendation to stop medical care or "
     "medication."),
    ("Ce n'est pas un conseil juridique ou financier",
     "Aucun avis sur un contrat, sur des droits, sur un placement ou sur un "
     "crédit.",
     "It is not legal or financial advice",
     "No opinion on a contract, on rights, on an investment or on credit."),
    ("Ce n'est pas une garantie",
     "Aucun résultat n'est promis. Une consultation qui promettrait un "
     "résultat mentirait.",
     "It is not a guarantee",
     "No outcome is promised. A consultation that promised one would be "
     "lying."),
    ("Ce n'est pas fondé sur la peur",
     "Aucune annonce de malheur, aucune urgence artificielle, aucun "
     "paiement présenté comme la condition d'un dénouement.",
     "It is not built on fear",
     "No announcement of misfortune, no artificial urgency, no payment "
     "presented as the condition of an outcome."),
    ("Ce n'est pas ouvert aux mineurs",
     "Le service est réservé aux personnes majeures.",
     "It is not open to minors",
     "The service is for adults only."),
]

APPROCHE_DONNEES = [
    ("On ne vous demande pas de raconter",
     "Le formulaire ne demande ni récit de santé, ni situation financière, "
     "ni dossier juridique, ni description de crise. Un motif en une ligne "
     "suffit pour fixer un rendez-vous.",
     "You are not asked to tell the story",
     "The form asks for no health account, no financial situation, no legal "
     "matter and no description of a crisis. One line is enough to arrange "
     "an appointment."),
    ("Deux consentements distincts",
     "Accepter d'être rappelé pour votre demande est une chose. Recevoir "
     "des communications commerciales en est une autre, et c'est une case "
     "séparée, jamais cochée d'avance.",
     "Two separate consents",
     "Agreeing to be contacted about your request is one thing. Receiving "
     "commercial messages is another, and it is a separate box, never "
     "pre-ticked."),
    ("Aucun ciblage publicitaire",
     "Rien de ce que vous confiez ne sert à vous cibler, ici ou ailleurs.",
     "No advertising targeting",
     "Nothing you share is used to target you, here or anywhere else."),
]

# ---------------------------------------------------------------------- FAQ
FAQ = [
    ("Comment se déroule une consultation ?",
     "Le déroulement exact — accueil, durée, forme de l'échange, suivi "
     "éventuel — sera décrit ici dès que le propriétaire l'aura arrêté. "
     "Écrire un déroulement plausible à sa place serait inventer.",
     "How does a consultation work?",
     "The exact process — welcome, length, form of the exchange, any "
     "follow-up — will be described here as soon as the owner has settled "
     "it. Writing a plausible version on their behalf would be inventing "
     "it."),
    ("Combien de temps dure une consultation ?",
     "À confirmer. C'est la décision D-02 du cahier des charges.",
     "How long does a consultation last?",
     "To be confirmed. This is decision D-02 of the specification."),
    ("Combien coûte une consultation ?",
     "À confirmer. Le tarif, les taxes, un dépôt éventuel et la politique "
     "de remboursement seront affichés ensemble et visibles avant toute "
     "confirmation — jamais après.",
     "How much does a consultation cost?",
     "To be confirmed. The price, taxes, any deposit and the refund policy "
     "will be shown together and visible before any confirmation — never "
     "after."),
    ("Faut-il préparer quelque chose ?",
     "À confirmer. En revanche une chose est déjà sûre : il n'est pas "
     "nécessaire d'écrire votre situation à l'avance, et le formulaire ne "
     "vous le demandera pas.",
     "Is there anything to prepare?",
     "To be confirmed. One thing is already certain: there is no need to "
     "write your situation down in advance, and the form will not ask you "
     "to."),
    ("Dans quelles langues se déroule la consultation ?",
     "À confirmer. Ce site existe en français et en anglais, mais la langue "
     "d'un site ne dit rien de la langue d'un entretien, et les deux ne "
     "doivent pas être confondues.",
     "What languages are consultations held in?",
     "To be confirmed. This site exists in French and English, but the "
     "language of a website says nothing about the language of a "
     "conversation, and the two must not be confused."),
    ("Les consultations à distance sont-elles possibles ?",
     "À confirmer — décision D-03. Tant que ce n'est pas tranché, aucune "
     "consultation par téléphone ou en vidéo n'est annoncée, pour ne pas "
     "promettre un service qui n'existerait pas.",
     "Are remote consultations possible?",
     "To be confirmed — decision D-03. Until this is settled, no phone or "
     "video consultation is announced, so as not to promise a service that "
     "may not exist."),
    ("Quels sont les horaires ?",
     "À confirmer — décision D-05. Le téléphone reste le moyen le plus sûr "
     "de savoir quand il est possible de venir.",
     "What are the opening hours?",
     "To be confirmed — decision D-05. The phone remains the surest way to "
     "find out when it is possible to come."),
    ("Comment annuler ou reporter ?",
     "À confirmer — décision D-05. La politique complète sera publiée sur "
     "la page Conditions de service et rappelée dans chaque confirmation.",
     "How do I cancel or reschedule?",
     "To be confirmed — decision D-05. The full policy will be published on "
     "the Terms of service page and repeated in every confirmation."),
    ("Est-ce que les résultats sont garantis ?",
     "Non, et ils ne peuvent pas l'être. Une consultation propose une "
     "perspective, pas une issue.",
     "Are results guaranteed?",
     "No, and they cannot be. A consultation offers a perspective, not an "
     "outcome."),
    ("Est-ce que cela remplace un médecin, un avocat ou un conseiller "
     "financier ?",
     "Non. En situation d'urgence, contactez les services compétents.",
     "Does this replace a doctor, a lawyer or a financial adviser?",
     "No. In an emergency, contact the appropriate services."),
    ("Le service est-il ouvert aux mineurs ?",
     "Non. Le service est réservé aux personnes majeures.",
     "Is the service open to minors?",
     "No. The service is for adults only."),
    ("Ce que je dis reste-t-il confidentiel ?",
     "Oui. Ce qui se dit pendant la consultation n'est pas partagé et n'est "
     "pas publié. Le site, de son côté, ne vous demande jamais d'écrire "
     "quoi que ce soit de sensible.",
     "Is what I say confidential?",
     "Yes. What is said during a consultation is not shared and not "
     "published. The site itself never asks you to write anything "
     "sensitive."),
]

# ------------------------------------------------------------- prendre RDV
RDV_INTRO = (
    "Le plus rapide est d'appeler. Le formulaire ci-dessous sert à demander "
    "un rendez-vous quand appeler n'est pas commode.",
    "Calling is quickest. The form below is for requesting an appointment "
    "when calling is not convenient.")

RDV_AVERTISSEMENT = (
    "N'écrivez rien de sensible ici. Pas de détail de santé, de finances, de "
    "dossier juridique ni de situation de crise. Un mot sur le sujet suffit ; "
    "le reste se dit de vive voix.",
    "Do not write anything sensitive here. No health details, no finances, "
    "no legal matter, no crisis situation. A word about the subject is "
    "enough; the rest is said in person.")

# (nom, libellé fr, libellé en, type, requis, aide fr, aide en)
CHAMPS = [
    ("prenom", "Prénom", "First name", "text", True,
     "Le prénom suffit.", "A first name is enough."),
    ("contact", "Téléphone ou autre moyen de vous joindre",
     "Phone number or another way to reach you", "text", True,
     "Le moyen que vous préférez.", "Whichever you prefer."),
    ("langue", "Langue de l'échange", "Language of the exchange",
     "select", True,
     "Sous réserve des langues parlées, à confirmer.",
     "Subject to the languages spoken, to be confirmed."),
    ("service", "Sujet de la consultation", "Subject of the consultation",
     "select", True,
     "Une orientation générale, pas un récit.",
     "A general direction, not a story."),
    ("dispo", "Vos disponibilités", "Your availability", "text", False,
     "Par exemple : en semaine, en fin de journée.",
     "For example: weekdays, late afternoon."),
    ("message", "Message (facultatif)", "Message (optional)", "textarea",
     False,
     "Deux lignes suffisent. Rien de sensible.",
     "Two lines are enough. Nothing sensitive."),
]

LANGUES_CHOIX = [("fr", "Français", "French"), ("en", "Anglais", "English"),
                 ("autre", "Autre — à préciser au téléphone",
                  "Other — to discuss by phone")]

CONSENTEMENTS = [
    ("traitement",
     "J'accepte que ces renseignements servent à me recontacter au sujet de "
     "cette demande.",
     "I agree that this information may be used to contact me about this "
     "request.", True),
    ("marketing",
     "Je souhaite aussi recevoir des communications commerciales. "
     "(Facultatif, et jamais coché d'avance.)",
     "I would also like to receive commercial messages. (Optional, and "
     "never pre-ticked.)", False),
]

RDV_ATTENTES = [
    ("Le formulaire n'envoie encore rien",
     "Il est complet, validé côté navigateur et prêt à être branché. Le "
     "destinataire dépend d'une adresse courriel professionnelle sur le "
     "domaine, qui reste à créer (décision D-08).",
     "The form does not send anything yet",
     "It is complete, validated in the browser and ready to be connected. "
     "The recipient depends on a professional email address on the domain, "
     "which is still to be created (decision D-08)."),
    ("Demande à confirmer ou réservation instantanée",
     "Décision D-04. La version présentée ici est la demande à confirmer : "
     "c'est la seule qui n'exige pas un agenda tenu à jour, et elle "
     "n'invente aucun créneau disponible.",
     "Request to confirm, or instant booking",
     "Decision D-04. What is shown here is the request-to-confirm path: it "
     "is the only one that does not require an up-to-date calendar, and it "
     "invents no available slot."),
    ("Dépôt en ligne",
     "Décision D-04 également. S'il est exigé, le paiement passera par un "
     "prestataire reconnu et le site ne conservera aucune donnée de carte.",
     "Online deposit",
     "Decision D-04 as well. If required, payment will go through a "
     "recognised provider and the site will store no card data."),
]

# --------------------------------------------------------------- contact
CONTACT_INTRO = (
    "Le téléphone est le moyen le plus direct.",
    "The phone is the most direct way.")

CONTACT_CARTE_NOTE = (
    "La carte interactive n'est pas intégrée à cette page. Une carte "
    "embarquée dépose des témoins avant que vous ayez consenti à quoi que "
    "ce soit, ce que l'article 8.1 du cahier des charges interdit. Le bouton "
    "ci-dessous ouvre l'itinéraire dans une carte externe, à votre "
    "initiative.",
    "The interactive map is not embedded on this page. An embedded map drops "
    "cookies before you have consented to anything, which section 8.1 of the "
    "specification forbids. The button below opens directions in an external "
    "map, at your initiative.")

CONTACT_ATTENTES = [
    ("Heures d'ouverture",
     "Décision D-05. Aucun horaire n'est affiché ni déclaré dans les "
     "données structurées tant qu'il n'est pas confirmé : un horaire faux "
     "envoie quelqu'un devant une porte fermée.",
     "Opening hours",
     "Decision D-05. No hours are shown or declared in the structured data "
     "until confirmed: wrong hours send someone to a closed door."),
    ("Courriel professionnel",
     "Décision D-08, à créer sur le domaine avant la mise en ligne.",
     "Professional email address",
     "Decision D-08, to be created on the domain before launch."),
    ("WhatsApp",
     "Décision D-07. Le numéro n'est présenté comme joignable sur WhatsApp "
     "que si le propriétaire confirme que la ligne est activée pour cet "
     "usage.",
     "WhatsApp",
     "Decision D-07. The number is only presented as reachable on WhatsApp "
     "if the owner confirms the line is enabled for it."),
    ("Distance et temps de marche depuis le métro",
     "Non mesurés, donc non affichés. La fiche indique la proximité du "
     "métro Côte-Vertu, elle ne donne pas de durée.",
     "Distance and walking time from the metro",
     "Not measured, so not shown. The listing states proximity to "
     "Côte-Vertu metro; it gives no duration."),
]

# ------------------------------------------------------------------- avis
AVIS_INTRO = (
    "Aucun avis n'est reproduit sur ce site, et c'est délibéré.",
    "No review is reproduced on this site, and that is deliberate.")

AVIS_TEXTE = [
    ("La fiche publique affiche une note. Le cahier des charges lui-même, à "
     "l'article 1.2, demande que le nombre d'avis soit vérifié avant toute "
     "reprise. Tant que cette vérification n'a pas eu lieu, ni la note ni le "
     "nombre ne sont repris ici : un chiffre recopié sans être vérifié est "
     "un chiffre inventé.",
     "The public listing shows a rating. The specification itself, in "
     "section 1.2, requires the number of reviews to be verified before any "
     "reuse. Until that verification has happened, neither the rating nor "
     "the count appears here: a figure copied without being checked is a "
     "figure invented."),
    ("Les témoignages suivront la même règle. Un témoignage n'est publié "
     "qu'avec l'autorisation écrite de la personne, daté, et sans détail "
     "permettant de la reconnaître contre son gré. Rien n'est repris "
     "automatiquement d'un réseau social.",
     "Testimonials will follow the same rule. A testimonial is published "
     "only with the person's written permission, dated, and without any "
     "detail that identifies them against their will. Nothing is pulled "
     "automatically from a social network."),
    ("En attendant, le lien ci-dessous mène à la source, où les avis "
     "peuvent être lus tels qu'ils sont, avec leur date.",
     "In the meantime, the link below leads to the source, where reviews can "
     "be read as they are, with their dates."),
]

# --------------------------------------------------------- confidentialité
CONF_INTRO = (
    "Ce que ce site collecte, ce qu'il n'a pas, et ce qui reste à décider.",
    "What this site collects, what it does not have, and what remains to be "
    "decided.")

CONF_FAITS = [
    ("Le site ne dépose aucun témoin",
     "Ni témoin de mesure, ni témoin publicitaire, ni témoin de session. "
     "C'est pour cette raison qu'il n'y a pas de bandière de consentement : "
     "il n'y aurait rien à consentir.",
     "The site sets no cookies",
     "No analytics cookie, no advertising cookie, no session cookie. That is "
     "why there is no consent banner: there would be nothing to consent to."),
    ("Aucune requête ne sort du domaine",
     "Les polices, les images et les scripts sont servis depuis le site "
     "lui-même. Aucune carte, aucune vidéo et aucun bouton de réseau social "
     "n'est chargé depuis un tiers.",
     "No request leaves the domain",
     "Fonts, images and scripts are served from the site itself. No map, no "
     "video and no social button is loaded from a third party."),
    ("Aucun outil de mesure n'est installé",
     "Pas de Google Analytics, pas d'équivalent. Si une mesure est ajoutée "
     "plus tard, elle ne captera ni le texte libre des messages ni aucun "
     "renseignement confidentiel — c'est l'article 8.2 du cahier des "
     "charges.",
     "No analytics tool is installed",
     "No Google Analytics, no equivalent. If measurement is added later, it "
     "will capture neither the free text of messages nor any confidential "
     "information — that is section 8.2 of the specification."),
    ("Le formulaire n'envoie encore rien",
     "Il valide côté navigateur et s'arrête là. Aucune donnée n'est "
     "transmise, stockée ni conservée à ce stade.",
     "The form does not send anything yet",
     "It validates in the browser and stops there. No data is transmitted, "
     "stored or retained at this stage."),
    ("Les liens externes sont des liens, pas des chargements",
     "Ouvrir la fiche ou l'itinéraire vous emmène sur un autre site, où "
     "d'autres règles s'appliquent. Rien ne part tant que vous ne cliquez "
     "pas.",
     "External links are links, not loads",
     "Opening the listing or the directions takes you to another site, where "
     "other rules apply. Nothing leaves until you click."),
]

CONF_ATTENTES = [
    ("Responsable de la protection des renseignements personnels",
     "Décision D-10 : nom, fonction et coordonnées professionnelles, à "
     "publier sur cette page.",
     "Privacy officer",
     "Decision D-10: name, role and professional contact details, to be "
     "published on this page."),
    ("Durée de conservation des demandes",
     "Décision D-10. Une durée est nécessaire pour que la suppression "
     "automatique puisse être programmée.",
     "Retention period for requests",
     "Decision D-10. A duration is needed before automatic deletion can be "
     "scheduled."),
    ("Fournisseurs et lieux d'hébergement",
     "À documenter dès que l'hébergeur et le service de courriel sont "
     "choisis, y compris toute communication hors Québec ou hors Canada.",
     "Providers and hosting locations",
     "To be documented as soon as the host and email service are chosen, "
     "including any communication outside Quebec or Canada."),
    ("Dénomination légale de l'entreprise et adresse de correspondance",
     "Nécessaires pour que les droits d'accès, de rectification et de "
     "retrait puissent réellement s'exercer.",
     "Legal business name and correspondence address",
     "Needed so that rights of access, correction and withdrawal can "
     "actually be exercised."),
]

CONF_JURIDIQUE = (
    "Cette page est une rédaction de travail. Le cahier des charges le dit "
    "lui-même : les exigences juridiques doivent être validées par un "
    "professionnel qualifié avant la mise en ligne. Ce texte n'est pas un "
    "avis juridique et ne remplace pas cette validation.",
    "This page is a working draft. The specification says so itself: legal "
    "requirements must be validated by a qualified professional before "
    "launch. This text is not legal advice and does not replace that "
    "validation.")

# ------------------------------------------------------------- conditions
COND_INTRO = (
    "Le cadre de la prestation, dit avant plutôt qu'après.",
    "The terms of the service, stated before rather than after.")

COND_POINTS = [
    ("Nature du service",
     "Une consultation de guidance spirituelle et astrologique, offerte à "
     "des fins de réflexion personnelle.",
     "Nature of the service",
     "A spiritual and astrological guidance consultation, offered for "
     "personal reflection."),
    ("Absence de garantie",
     "Aucun résultat n'est garanti, et aucune somme n'est présentée comme la "
     "condition d'un dénouement.",
     "No guarantee",
     "No outcome is guaranteed, and no sum of money is presented as the "
     "condition of any outcome."),
    ("Âge",
     "Le service est réservé aux personnes majeures.",
     "Age",
     "The service is for adults only."),
    ("Prise de rendez-vous",
     "Une demande envoyée depuis le site est une demande, pas une "
     "réservation. Un rendez-vous n'existe qu'une fois confirmé.",
     "Booking",
     "A request sent from this site is a request, not a booking. An "
     "appointment exists only once confirmed."),
    ("Comportement",
     "La consultation peut être interrompue si le cadre n'est pas respecté, "
     "d'un côté comme de l'autre.",
     "Conduct",
     "A consultation may be ended if the framework is not respected, on "
     "either side."),
]

COND_ATTENTES = [
    ("Tarifs, taxes et dépôt",
     "Décision D-02. Ils seront visibles avant toute confirmation.",
     "Prices, taxes and deposit",
     "Decision D-02. They will be visible before any confirmation."),
    ("Politique d'annulation et de remboursement",
     "Décision D-05, avec les délais exacts.",
     "Cancellation and refund policy",
     "Decision D-05, with exact time limits."),
    ("Dénomination légale, adresse et immatriculation",
     "Nécessaires pour que ces conditions désignent quelqu'un.",
     "Legal name, address and registration",
     "Needed so that these terms name someone."),
]

# ----------------------------------------------------------- accessibilité
ACCESS_INTRO = (
    "Objectif WCAG 2.2 niveau AA. Ce qui a été mesuré, et ce qui ne l'a pas "
    "encore été.",
    "Target: WCAG 2.2 level AA. What has been measured, and what has not "
    "been yet.")

ACCESS_FAIT = [
    ("Contrastes mesurés, pas estimés",
     "Chaque couleur de texte a été mesurée sur le fond réel derrière elle, "
     "après rendu dans un navigateur. Les valeurs figurent dans le dossier "
     "de vérification livré avec le site.",
     "Contrast measured, not estimated",
     "Every text colour was measured against the actual background behind "
     "it, after rendering in a browser. The values are in the verification "
     "report delivered with the site."),
    ("Navigation au clavier complète",
     "Un lien d'évitement en tête de page, un ordre de tabulation logique, "
     "un focus toujours visible, et le menu mobile qui se referme à Échap.",
     "Full keyboard navigation",
     "A skip link at the top of each page, a logical tab order, a focus "
     "outline that is always visible, and a mobile menu that closes on "
     "Escape."),
    ("Zoom à 200 % sans perte",
     "Aucun défilement horizontal jusqu'à 320 pixels de large, ce qui "
     "correspond au zoom à 200 % sur un écran courant.",
     "200 % zoom without loss",
     "No horizontal scrolling down to 320 pixels wide, which corresponds to "
     "200 % zoom on a common screen."),
    ("Mouvement réductible",
     "Les animations s'arrêtent si le système déclare préférer moins de "
     "mouvement.",
     "Reducible motion",
     "Animations stop if the system declares a preference for reduced "
     "motion."),
    ("Formulaire annonçable",
     "Chaque champ a une étiquette liée, chaque erreur est annoncée, et le "
     "texte saisi est conservé quand une erreur survient.",
     "Announceable form",
     "Every field has a linked label, every error is announced, and typed "
     "text is kept when an error occurs."),
]

ACCESS_PAS_FAIT = [
    ("Test avec de vraies personnes utilisant un lecteur d'écran",
     "Les vérifications automatiques et un passage au clavier ne remplacent "
     "pas un test avec des personnes concernées.",
     "Testing with real screen-reader users",
     "Automated checks and a keyboard pass do not replace testing with the "
     "people concerned."),
    ("Les filets dorés décoratifs",
     "Ils mesurent 2,18:1 sur l'ivoire, sous le seuil de 3:1. Ils ne "
     "portent aucune information : retirés, rien ne devient inutilisable. "
     "Tout élément qui porte une information — bordure de champ, contour de "
     "focus, bouton — utilise une couleur mesurée au-dessus du seuil.",
     "The decorative gold hairlines",
     "They measure 2.18:1 on ivory, below the 3:1 threshold. They carry no "
     "information: removed, nothing becomes unusable. Anything that does "
     "carry information — field borders, focus outlines, buttons — uses a "
     "colour measured above the threshold."),
    ("Les contenus qui n'existent pas encore",
     "Photographies, témoignages et documents à venir devront être "
     "accessibles à leur tour : texte alternatif réel, transcription si "
     "audio, et pas de renseignement personnel dans une image.",
     "Content that does not exist yet",
     "Photographs, testimonials and future documents will have to be "
     "accessible in turn: real alternative text, a transcript if audio, and "
     "no personal information inside an image."),
]

# ------------------------------------------------------------------- pied
PIED_DECLARATION = (
    "Site de démonstration. Les contenus marqués « À confirmer » attendent "
    "la validation du propriétaire et ne doivent pas être considérés comme "
    "définitifs.",
    "Demonstration site. Content marked “To be confirmed” is awaiting the "
    "owner's validation and should not be treated as final.")

PIED_LANGUE = ("Français", "English")

# ---------------------------------------------------------- méta (SEO local)
META = {
    "accueil": (
        "Guidance spirituelle et astrologique à Saint-Laurent, près du métro "
        "Côte-Vertu. Consultation confidentielle sur les enjeux d'affaires, "
        "la carrière, les finances et les partenariats.",
        "Spiritual and astrological guidance in Saint-Laurent, near "
        "Côte-Vertu metro. Confidential consultations on business matters, "
        "career, finances and partnerships."),
    "services": (
        "Les quatre consultations proposées au lancement : enjeux "
        "d'affaires, croissance et carrière, préoccupations financières, "
        "partenariats. Durées et tarifs à confirmer.",
        "The four consultations offered at launch: business matters, growth "
        "and career, financial concerns, partnerships. Durations and prices "
        "to be confirmed."),
    "svc-affaires": (
        "Une consultation pour poser à plat une décision d'affaires. Ni avis "
        "juridique, ni plan d'affaires, ni garantie sur l'issue.",
        "A consultation to lay out a business decision. Not legal advice, "
        "not a business plan, and no guarantee about the outcome."),
    "svc-carriere": (
        "Une consultation autour d'une transition professionnelle ou d'un "
        "changement de cap. Ni orientation certifiée, ni accompagnement "
        "thérapeutique.",
        "A consultation around a professional transition or a change of "
        "direction. Not certified career guidance, not therapy."),
    "svc-finances": (
        "Une réflexion astrologique autour d'une préoccupation financière. "
        "Ce n'est pas du conseil financier et aucune prévision de gain n'est "
        "faite.",
        "An astrological reflection around a financial concern. This is not "
        "financial advice and no forecast of gain is made."),
    "svc-partenariats": (
        "Une consultation sur la dynamique d'un partenariat d'affaires. Ni "
        "médiation, ni arbitrage, ni avis sur un contrat.",
        "A consultation on the dynamics of a business partnership. Not "
        "mediation, not arbitration, no opinion on a contract."),
    "apropos": (
        "Parcours, méthodes, certifications et photographie du praticien : "
        "ce qui n'a pas été fourni n'est pas inventé, et la page dit ce "
        "qu'elle attend.",
        "Background, methods, certifications and photograph of the "
        "practitioner: what was not provided is not invented, and the page "
        "states what it is waiting for."),
    "approche": (
        "Confidentialité, consentement, limites et absence de garantie. Ce "
        "que la consultation est, et ce qu'elle n'est pas.",
        "Confidentiality, consent, limits and the absence of any guarantee. "
        "What a consultation is, and what it is not."),
    "faq": (
        "Déroulement, durée, tarif, préparation, langues, annulation et "
        "consultations à distance. Les réponses encore inconnues sont "
        "marquées comme telles.",
        "Process, length, price, preparation, languages, cancellation and "
        "remote consultations. Answers not yet known are marked as such."),
    "reserver": (
        "Demander un rendez-vous à Saint-Laurent, ou appeler directement. Le "
        "formulaire ne demande aucun renseignement sensible.",
        "Request an appointment in Saint-Laurent, or call directly. The form "
        "asks for no sensitive information."),
    "contact": (
        "1485, rue MacDonald, Saint-Laurent, près du métro Côte-Vertu. "
        "Téléphone, adresse et itinéraire, sans carte embarquée ni témoin.",
        "1485 MacDonald Street, Saint-Laurent, near Côte-Vertu metro. Phone, "
        "address and directions, with no embedded map and no cookies."),
    "avis": (
        "Aucun avis n'est reproduit ici tant que le nombre n'a pas été "
        "vérifié et que les témoignages n'ont pas été autorisés par écrit.",
        "No review is reproduced here until the count has been verified and "
        "testimonials have been authorised in writing."),
    "confidentialite": (
        "Aucun témoin, aucune requête hors du domaine, aucun outil de "
        "mesure. Ce qui reste à décider avant la mise en ligne est listé.",
        "No cookies, no request outside the domain, no analytics. What "
        "remains to be decided before launch is listed."),
    "conditions": (
        "Nature du service, absence de garantie, âge requis et prise de "
        "rendez-vous. Tarifs et politique d'annulation à confirmer.",
        "Nature of the service, absence of any guarantee, age requirement "
        "and booking. Prices and cancellation policy to be confirmed."),
    "accessibilite": (
        "Objectif WCAG 2.2 AA : contrastes mesurés, navigation au clavier, "
        "zoom à 200 %. Ce qui n'a pas encore été testé est dit aussi.",
        "Target WCAG 2.2 AA: measured contrast, keyboard navigation, 200 % "
        "zoom. What has not been tested yet is stated too."),
}
