# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""
from Regle import regle
from CompareCarteJeu import compareCarteJeu
def pliHumain(jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, num_joueur):
    autorise = False
    while not autorise:
        print("Cartes jouées :", cartes_pli)
        print("Atout :" + couleur_atout)
        print("Mon jeu :")
        for i in range(len(jeu)):
            print(i + 1, ":", jeu[i], "\n")
        choix = input("Quelle carte jouer ?")
        choix = int(choix)
        if choix > 8-num_pli:
            print("Ce numéro n'est pas autorisé")
        elif regle(jeu, cartes_pli, jeu[choix-1], couleur_atout, carte_meneuse):
            autorise = True
        else:
            print("Vous n'êtes pas autorisé à jouer cette carte")
    if jeu[choix-1][1]==couleur_atout and jeu[choix-1][0] in ["Dame", "Roi"] and belote==4:
        belote = input("Belote ? (y/n)")
        while belote != "y" and belote != "n":
            print("Argument non valide")
            belote = input("Belote ? (y/n)")
    elif jeu[choix-1][1]==couleur_atout and jeu[choix-1][0] in ["Dame", "Roi"] and belote==num_joueur:
        rebelote = input("Rebelote ? (y/n)")
        while rebelote != "y" and rebelote != "n":
            print("Argument non valide")
            rebelote = input("Rebelote ? (y/n)")
    cartes_pli.append(jeu[choix-1])
    if belote == "y":
        belote = num_joueur
    if rebelote == "y":
        rebelote == num_joueur
    jeu.pop(choix-1)
    return jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse
