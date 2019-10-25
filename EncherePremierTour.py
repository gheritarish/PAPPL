# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:42:04 2019

@author: telmar
"""

def encherePremierTour(jeu1, jeu2, jeu3, jeu4, carte,joueur):
     """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
     print("premier tour d'enchere")
     for i in range(4):
         print(joueur[i])
         if i == 0:
             print('votre jeu')
             print(jeu1, "\n")
         elif i == 1:
             print('votre jeu')
             print(jeu2, "\n")
         elif i == 2:
             print('votre jeu')
             print(jeu3, "\n")
         elif i == 3:
             print('votre jeu')
             print(jeu4, "\n")
         print(carte)
         res = input("Voulez-vous prendre ? (y/n)")
         if res == "y":
             return [i, carte[1]]
     return ["Personne n'a pris"]
