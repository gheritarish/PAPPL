# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:45:55 2019

@author: telmar
"""

def EnchereDeuxiemeTour(jeu1, jeu2, jeu3, jeu4, carte):
    """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
    for i in range(4):
         if i == 0:
             for elt in jeu1:
                print(elt[0], elt[1], "\n")
        elif i == 1:
            for elt in jeu2:
                print(elt[0], elt[1], "\n")
        elif i == 2:
            for elt in jeu3:
                print(elt[0], elt[1], "\n")
        elif i == 3:
            for elt in jeu4:
                print(elt[0], elt[1], "\n")
        prise = input("Voulez-vous prendre ? (y/n)")
        if prise == "y":
            couleur = carte[1]
            if couleur == "pique":
                print("1. Trèfle \n2. Carreau \n3. Coeur")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return [i, "trèfle"]
                elif coul_choisie == 2:
                    return [i, "carreau"]
                else:
                    return [i, "coeur"]
            elif couleur == "trèfle":
                print("1. Pique \n2. Carreau \n3. Coeur")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return [i, "pique"]
                elif coul_choisie == 2:
                    return [i, "carreau"]
                else:
                    return [i, "coeur"]
            elif couleur == "carreau":
                print("1. Trèfle \n2. Pique \n3. Coeur")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return [i, "trèfle"]
                elif coul_choisie == 2:
                    return [i, "pique"]
                else:
                    return [i, "coeur"]
            else:
                print("1. Trèfle \n2. Pique \n3. Carreau")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return [i, "trèfle"]
                elif coul_choisie == 2:
                    return [i, "pique"]
                else:
                    return [i, "carreau"]
    return ["Personne n'a pris"]
 
