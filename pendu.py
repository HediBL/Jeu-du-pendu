#Ce fichier contien le jeu du pendu

from donnees import *
from fonctions import *

#Je récupère les scores de la partie
scores = recup_scores()

#Je récupère les noms d'utilisateur
utilisateur = recup_nom_utilisateur()

#Si le score de l'utilisateur n'existe pas, on l'ajoute
if utilisateur not in scores.keys()
    scores[utilisateur] = 0

#Pour savoir quand arreter la partie
continuer_partie = 'o'

while continuer_partie != 'n'
    print("Joueur {0}: {1} point(s)". format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettre_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances= nb_coups
    while mot_a_trouver != mot_trouve and nb_chances>0:
        print("Mot à trouver{0} (encore{1} chances)". format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettre_trouvees: #la lettre a deja ete choisie
            print("Vous avez déjà choisi cette lettre")
        elif lettre in mot_a_trouver: #la lettre est dans le mot à trouver
            lettre_trouvees.append(lettre)
            print("Bien joué!")
        else:
            nb_chances -=1
            print("...non, cette lettre ne se trouve pas dans le mot")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettre_trouvees)

        #A t-il trouver le mot ou ses chances sont épuisées
    if mot_a_trouver == mot_trouve
    print("Félicitations! Vous avez trouvé le mot{0}.".format(mot_a_trouver))
    else:
        print("PENDU!!! Vous avez perdu.")

    #Je mets à jour le score de l'utilisateur
    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N)?")
    continuer_partie = continuer_partie.lower()

#La partie est terminée. Enregistrement des scores
enregistrer_scores(scores)

#Affichage des scores de l'utilisateur
print("Vous terminez la partie avec {0} points.".format(scores[utilisateur]))

