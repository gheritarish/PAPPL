# -*- coding: utf-8 -*-
"""
Created on Fri Nov 08 14:36:55 2019

@author: telmar
"""

import random as rd
from AffichageTexte import affichageTexte
from AffichageDistribution import affichageDistribution
from AffichageOuiNon import affichageOuiNon

def enchereDeuxiemeTourIA(jeu1, jeu2, jeu3, jeu4, carte,joueur):
    """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
    affichageTexte("second tour d'enchere")
    for i in range(4):
        couleur = carte[1]
        if joueur[i][1] != "IAaleatoire" and joueur[i][1] != "IAminimax":
            affichageTexte("c\'est au tour de: "+ joueur[i][0])
            if i == 0:
                prise =  affichageDistribution(jeu1,carte,joueur[i][0],1)
            elif i == 1:
                prise =  affichageDistribution(jeu2,carte,joueur[i][0],1)
            elif i == 2:
                prise =  affichageDistribution(jeu3,carte,joueur[i][0],1)
            elif i == 3:
                prise =  affichageDistribution(jeu4,carte,joueur[i][0],1)
            if prise == "y": # Si l'IA prend, elle choisit quelle couleur sera l'atout
                if couleur == "pique":
                    coul_choisie = int(affichageOuiNon("Choisissez le numéro de la couleur : 1. Trèfle 2. Carreau 3. Coeur",["1","2","3"]))
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "trèfle":
                    coul_choisie = int(affichageOuiNon("Choisissez le numéro de la couleur: 1. Pique 2. Carreau 3. Coeur",["1","2","3"]))
                    if coul_choisie == 1:
                        return [i, "pique"]
                    elif coul_choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "carreau":
                    coul_choisie = int(affichageOuiNon("Choisissez le numéro de la couleur: 1. Trèfle 2. Pique 3. Coeur",["1","2","3"]))
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "coeur"]
                else:
                    coul_choisie = int(affichageOuiNon("Choisissez le numéro de la couleur: 1. Trèfle 2. Pique 3. Carreau",["1","2","3"]))
                    if coul_choisie == 1:
                        return [i, "trèfle"]
                    elif coul_choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "carreau"]
        
        else:
            choisie = rd.randint(1,4)
            if choisie != 4:
                if couleur == "pique":
                    if choisie == 1:
                        return [i, "trèfle"]
                    elif choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "trèfle":
                    if choisie == 1:
                        return [i, "pique"]
                    elif choisie == 2:
                        return [i, "carreau"]
                    else:
                        return [i, "coeur"]
                elif couleur == "carreau":
                    if choisie == 1:
                        return [i, "trèfle"]
                    elif choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "coeur"]
                else:
                    if choisie == 1:
                        return [i, "trèfle"]
                    elif choisie == 2:
                        return [i, "pique"]
                    else:
                        return [i, "carreau"]
    return ["Personne n'a pris"]
 
