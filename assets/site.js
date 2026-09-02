/* Master Skanda — le seul script du site.
   Pas de bibliothèque, pas de requête réseau, pas de témoin. */
(function () {
  "use strict";

  var fr = (document.documentElement.lang || "fr").slice(0, 2) === "fr";

  function txt(f, e) { return fr ? f : e; }

  /* ------------------------------------------------------------- menu */
  var burger = document.querySelector(".burger");
  var panneau = document.getElementById("panneau-nav");

  function ferme() {
    if (!burger || !panneau) return;
    panneau.classList.remove("ouvert");
    burger.setAttribute("aria-expanded", "false");
  }

  if (burger && panneau) {
    burger.addEventListener("click", function () {
      var ouvert = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", ouvert ? "false" : "true");
      panneau.classList.toggle("ouvert", !ouvert);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" &&
          burger.getAttribute("aria-expanded") === "true") {
        ferme();
        burger.focus();
      }
    });
    document.addEventListener("click", function (e) {
      if (burger.getAttribute("aria-expanded") !== "true") return;
      if (panneau.contains(e.target) || burger.contains(e.target)) return;
      ferme();
    });
    /* Le panneau est masqué par une media query au-delà de 1000 px. S'il
       reste « ouvert » dans l'attribut pendant qu'il est masqué, le bouton
       ment aux technologies d'assistance. */
    var large = window.matchMedia("(min-width:1001px)");
    var surveille = function (m) { if (m.matches) ferme(); };
    if (large.addEventListener) large.addEventListener("change", surveille);
    else if (large.addListener) large.addListener(surveille);
  }

  /* -------------------------------------------------------- formulaire */
  var form = document.querySelector(".formulaire");
  if (!form) return;

  var etat = document.getElementById("form-etat");

  function erreur(champ, message) {
    var boite = champ.closest(".champ");
    var cible = document.getElementById("e-" + champ.name);
    if (boite) boite.classList.toggle("faux", !!message);
    if (cible) cible.textContent = message || "";
    if (message) champ.setAttribute("aria-invalid", "true");
    else champ.removeAttribute("aria-invalid");
  }

  function valide(champ) {
    var v = (champ.value || "").trim();
    if (champ.type === "checkbox") {
      if (champ.required && !champ.checked) {
        return txt("Cette case doit être cochée pour envoyer la demande.",
                   "This box must be ticked to send the request.");
      }
      return "";
    }
    if (champ.required && !v) {
      return txt("Ce champ est obligatoire.", "This field is required.");
    }
    if (champ.name === "contact" && v && v.length < 6) {
      return txt("Indiquez un moyen de vous joindre, en entier.",
                 "Please give a complete way to reach you.");
    }
    return "";
  }

  var champs = Array.prototype.slice.call(
    form.querySelectorAll("input, select, textarea"));

  champs.forEach(function (c) {
    c.addEventListener("blur", function () { erreur(c, valide(c)); });
    c.addEventListener("input", function () {
      if (c.getAttribute("aria-invalid")) erreur(c, valide(c));
    });
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var premier = null;
    champs.forEach(function (c) {
      var m = valide(c);
      erreur(c, m);
      if (m && !premier) premier = c;
    });
    if (premier) {
      if (etat) etat.textContent = "";
      premier.focus();
      return;
    }
    /* Le formulaire est complet et validé, et il s'arrête ici. Il n'y a
       pas de destinataire tant qu'aucune adresse professionnelle n'existe
       sur le domaine (décision D-08). Prétendre l'avoir envoyé serait un
       mensonge, et un mensonge qui coûte un rendez-vous. */
    if (etat) {
      etat.textContent = txt(
        "Formulaire validé. L'envoi n'est pas encore branché : aucune " +
        "adresse professionnelle n'existe pour l'instant sur le domaine. " +
        "Pour un rendez-vous aujourd'hui, appelez le " +
        document.body.getAttribute("data-tel") + ".",
        "Form validated. Sending is not connected yet: there is no " +
        "professional address on the domain at this stage. For an " +
        "appointment today, please call " +
        document.body.getAttribute("data-tel") + ".");
      etat.focus && etat.focus();
    }
  });
})();
