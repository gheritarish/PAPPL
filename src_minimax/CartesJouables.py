# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:27:10 2019

@author: alepe
"""
from Regle import regle

def cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse):
    """Fonction qui renvoie les cartes que peut jouer l'IA. Elle prend en arguments les cartes de l'IA, les cartes du pli actuel, la couleur de l'atout et la carte meneuse"""
    cartes_possibles=[] # Va nous donner les cartes que peut jouer l'IA
    for i in range(len(cartesIA)):
        if regle(cartesIA, cartes_pli, cartesIA[i], couleur_atout, carte_meneuse):
            cartes_possibles.append(i)
    return cartes_possibles # On renvoie la liste des cartes possibles
