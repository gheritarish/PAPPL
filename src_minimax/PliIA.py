# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""
from Regle import regle
from CompareCarteJeu import compareCarteJeu
import random as rd
from CartesJouables import cartesJouables

def pliIA(jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, num_joueur):
    autorise=False
    cartes_possibles = cartesJouables(jeu, cartes_pli, couleur_atout, carte_meneuse)
    jouer = rd.randint(1, len(cartes_possibles))
    card = cartes_possibles[jouer-1]
    cartes_pli.append(jeu[card])
    if jeu[card][1] == couleur_atout and jeu[card][0] in ["Dame", "Roi"] and belote == 4:
         belote = 0
        elif jeu[card][1] == couleur_atout and jeu[card][0] in ["Dame", "Roi"] and belote == 0:
        rebelote = 0
    jeu.pop(card)
    return jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse
