# -*- coding: utf-8 -*-
"""
Created on Fri Nov 08 14:23:04 2019

@author: telmar
"""
from AffichageTexte import affichageTexte
from AffichageDistribution import affichageDistribution
import random as rd

def encherePremierTourIA(jeu1, jeu2, jeu3, jeu4, carte,joueur):
    """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
    #affichageTexte("premier tour d'enchere")
    for i in range(4):
        if joueur[i][1] != "IAaleatoire" and joueur[i][1] != "IAminimax":
            affichageTexte("c\'est au tour de: "+joueur[i][0])
            if i == 0:
                prise =  affichageDistribution(jeu1,carte,joueur[i][0],1)
            elif i == 1:
                prise =  affichageDistribution(jeu2,carte,joueur[i][0],1)
            elif i == 2:
                prise =  affichageDistribution(jeu3,carte,joueur[i][0],1)
            elif i == 3:
                prise =  affichageDistribution(jeu4,carte,joueur[i][0],1)
            
            if prise == "y": # Si quelqu'un prend, on renvoie le joueur et l'atout
                return [i, carte[1]]
        else: # Si le joueur est une IA, elle tire au hasard si elle prend ou pas
            prise = rd.randint(1,2)
            if prise == 1:
                return [i, carte[1]]
    return ["Personne n'a pris"]
