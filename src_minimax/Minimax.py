# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:31:29 2019

@author: alepe
"""
from cartesJouables import cartesJouables
from SuppressionCartes import suppressionCartes

def minimax(cartesIA, paquet,couleur_atout,carte_meneuse, cartes_pli):
    cartes_possibles=cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse) # on recupère les cartes jouables
    cartesAutreJoueur=suppressionCartes(suppressionCartes(paquet,cartes_pli), cartesIA)
    
    
    