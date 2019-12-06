# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:44:59 2019

@author: alepe
"""

from Regle import regle
from CompareCarteJeu import compareCarteJeu
import random as rd
from CartesJouables import cartesJouables
from Minimax import minimax

def pliIAminimax(jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, num_joueur,difficulte,meneur,preneur):
    """Fonction qui permet à une IA naïve de jouer. Prend en arguments le jeu de l'IA, les cartes du pli, le joueur qui a fait une belote et une rebelote, la couleur de l'atout, la carte meneuse, le numéro du pli et le numéro du joueur"""
    autorise=False
    poids=minimax(jeu, paquet,couleur_atout,carte_meneuse,meneur, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,preneur)
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