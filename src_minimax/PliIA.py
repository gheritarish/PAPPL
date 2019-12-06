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
    """Fonction qui permet à une IA naïve de jouer. Prend en arguments le jeu de l'IA, les cartes du pli, le joueur qui a fait une belote et une rebelote, la couleur de l'atout, la carte meneuse, le numéro du pli et le numéro du joueur"""
    autorise=False
    cartes_possibles = cartesJouables(jeu, cartes_pli, couleur_atout, carte_meneuse) # On fait la liste des indices des cartes que l'IA peut jouer
    jouer = rd.randint(1, len(cartes_possibles)) # On choisit un indice de cartes au hasard parmi ces indices
    card = cartes_possibles[jouer-1] # L'indice définit la carte
    cartes_pli.append(jeu[card])
    if jeu[card][1] == couleur_atout and jeu[card][0] in ["Dame", "Roi"] and belote == 4: # Si c'est une situation de belote, l'IA la déclare immédiatement
        belote = 0
    elif jeu[card][1] == couleur_atout and jeu[card][0] in ["Dame", "Roi"] and belote == num_joueur: # Si c'est une situation de rebelote, l'IA la déclare immédiatement
        rebelote = 0
    jeu.pop(card) # On enlève la carte jouée du jeu de l'IA
    return jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse
