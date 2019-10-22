# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:45:55 2019

@author: telmar
"""

def EnchereDeuxiemeTour(jeu1, jeu2, jeu3, jeu4, carte):
    for i in range(4):
        prise = input("Voulez-vous prendre ? (y/n)")
        if prise == "y":
            couleur = carte[1]
            if couleur == "pique":
                print("1. Trèfle \n2. Carreau \n3. Coeur")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return i, "trèfle"
                elif coul_choisie == 2:
                    return i, "carreau"
                else:
                    return i, "coeur"
            elif couleur == "trèfle":
                print("1. Pique \n2. Carreau \n3. Coeur")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return i, "pique"
                elif coul_choisie == 2:
                    return i, "carreau"
                else:
                    return i, "coeur"
            elif couleur == "carreau":
                print("1. Trèfle \n2. Pique \n3. Coeur")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return i, "trèfle"
                elif coul_choisie == 2:
                    return i, "pique"
                else:
                    return i, "coeur"
            else:
                print("1. Trèfle \n2. Pique \n3. Carreau")
                coul_choisie = input("Choisissez le numéro de la couleur")
                if coul_choisie == 1:
                    return i, "trèfle"
                elif coul_choisie == 2:
                    return i, "pique"
                else:
                    return i, "carreau"
    return "Personne n'a pris"
 
