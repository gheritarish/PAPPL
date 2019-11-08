# -*- coding: utf-8 -*-
"""
Created on Fri Nov 08 14:36:55 2019

@author: telmar
"""

import random as rd

def enchereDeuxiemeTourIA(jeu1, jeu2, jeu3, jeu4, carte,joueur):
    """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
    print("second tour d'enchere")
    for i in range(4):
        if joueur[i][1] != "IA":
            print("c\'est au tour de: "+ joueur[i])
            if i == 0:
                print(jeu1, "\n")
            elif i == 1:
                print(jeu2, "\n")
            elif i == 2:
                print(jeu3, "\n")
            elif i == 3:
                print(jeu4, "\n")
            print(carte)
            prise = input("Voulez-vous prendre ? (y/n)")
            if prise == "y":
                couleur = carte[1]
                if couleur == "pique":
                    print("1. Trèfle \n2. Carreau \n3. Coeur")
                    coul_choisie = int(input("Choisissez le numéro de la couleur"))
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "trèfle":
                    print("1. Pique \n2. Carreau \n3. Coeur")
                    coul_choisie = int(input("Choisissez le numéro de la couleur"))
                    if coul_choisie == 1:
                        return [i, "pique"]
                    elif coul_choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "carreau":
                    print("1. Trèfle \n2. Pique \n3. Coeur")
                    coul_choisie = int(input("Choisissez le numéro de la couleur"))
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                    return [i, "pique"]
                    else:
                        return [i, "coeur"]
                else:
                    print("1. Trèfle \n2. Pique \n3. Carreau")
                    coul_choisie = int(input("Choisissez le numéro de la couleur"))
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "carreau"]
        else:
            coul_choisie = rd.random(1,4)
            if coul_choisie != 4:
                if couleur == "pique":
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "trèfle":
                    if coul_choisie == 1:
                        return [i, "pique"]
                    elif coul_choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "carreau":
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "coeur"]
                else:
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "carreau"]
    return ["Personne n'a pris"]
 
