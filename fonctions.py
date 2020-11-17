#Ce fichier contien les fonctions utiles (les actions du programme)

import os
import pickle
from random import choice
from donnees import *

#Gestion des scores
def recup_scores():
    if os.path.exists(nom_fichier_scores): #le fichier existe
    #on le récupère

        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: #le fichier n'existe pas
        scores = {}
    return scores

def enregistrer_scores(scores):
    fichier_scores = open(nom_fichiers_scores, "wb")#j'écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

#Fonctions gérant les éléments saisis par l'utilisateur

def recup_nom_utilisateur():
    nom_utilisateur = input("Tapez votre nom")
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide")
        #j'appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        recup_nom_utilisateur

def recup_lettre():
    #cette fonction récupère une lettre saisie par l'utilisateur
    #si la chaine n'est pas une lettre on rappelle la fonction
    #jusqu'à avoir une lettre

    lettre = input("Tapez une lettre")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalnum():
        print("Vous n'avez pas saisi une lettre valide")
        return recup_lettre()
    else:
        return lettre

#Fonctions du jeu

def choisir_mot():
    #cette fonction renvoi le mot choisi dans la liste des mots
    return choice(liste_mots_aleatoires)

def recup_mot_masque(mot_complet, lettre_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettre_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque

