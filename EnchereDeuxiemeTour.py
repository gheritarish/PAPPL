# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:45:55 2019

@author: telmar
"""

def enchereDeuxiemeTour(jeu1, jeu2, jeu3, jeu4, carte,joueur):
    """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
    print("second tour d'enchere")
    for i in range(4):
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
         if prise == "y": # Si quelqu'un prend, on lui demande à quelle couleur il souhaite prend
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
    return ["Personne n'a pris"]
 
