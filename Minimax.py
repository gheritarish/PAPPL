# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:31:29 2019

@author: alepe
"""
from CartesJouables import cartesJouables
from SuppressionCartes import suppressionCartes
from RedistributionIA import redistributionIA
from numpy import np

def minimax(cartesIA, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte):
    cartes_possibles=cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse) # on recupère les cartes jouables
    cartesAutreJoueur=suppressionCartes(suppressionCartes(paquet,cartes_pli), cartesIA) #cartes à redistribuer
    poids=np.zeros(len(cartes_possibles)) #matrice des poids de chaque cartes
    for i in range(difficulte):
        jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli))
    
    
    