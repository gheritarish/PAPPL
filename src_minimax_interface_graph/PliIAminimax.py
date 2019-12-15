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
from CreationPaquetDeCartes import creationPaquetDeCartes
from SuppressionCartes import suppressionCartes
import numpy as np


def pliIAminimax(jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_joueur,difficulte,meneur,preneur,plis_equipe1,plis_equipe2):
    """Fonction qui permet à une IA naïve de jouer. Prend en arguments le jeu de l'IA, les cartes du pli, le joueur qui a fait une belote et une rebelote, la couleur de l'atout, la carte meneuse, le numéro du pli et le numéro du joueur"""
    paquet = creationPaquetDeCartes()
    for k in range (len(plis_equipe1)):
        paquet = suppressionCartes(paquet,plis_equipe1[k])
    for k in range (len(plis_equipe2)):
        paquet = suppressionCartes(paquet,plis_equipe2[k])
    if belote ==4:
        belotebis = 4
    else :
        belotebis = (belote -(num_joueur-len(cartes_pli))%4)%4
    if rebelote==4:
        rebelotebis=4
    else :
        rebelotebis = (rebelote -(num_joueur-len(cartes_pli))%4)%4
    poids=minimax(jeu, paquet,couleur_atout,carte_meneuse,meneur, cartes_pli,difficulte,belotebis,rebelotebis,plis_equipe1,plis_equipe2,preneur)
    cartes_possibles = cartesJouables(jeu, cartes_pli, couleur_atout, carte_meneuse) # On fait la liste des indices des cartes que l'IA peut jouer
    jouer = np.argmax(poids) # On choisit un indice de cartes au hasard parmi ces indices
    card = cartes_possibles[jouer] # L'indice définit la carte
    cartes_pli.append(card)
    
    if card[1] == couleur_atout and card[0] in ["Dame", "Roi"] and belote == 4: # Si c'est une situation de belote, l'IA la déclare immédiatement
        belote = num_joueur
    elif card[1] == couleur_atout and card[0] in ["Dame", "Roi"] and belote == num_joueur: # Si c'est une situation de rebelote, l'IA la déclare immédiatement
        rebelote = num_joueur
    jeu.pop(jeu.index(card)) # On enlève la carte jouée du jeu de l'IA
    return jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse
