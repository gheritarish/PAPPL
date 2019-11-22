# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:31:29 2019

@author: alepe
"""
from CartesJouables import cartesJouables
from SuppressionCartes import suppressionCartes
from RedistributionIA import redistributionIA
from numpy import np
from JeuDeLaCarteMinimax import jeuDeLaCarteMinimax


def minimax(cartesIA, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli):
    cartes_possibles=cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse) # on recupère les cartes jouables
    cartesAutreJoueur=suppressionCartes(suppressionCartes(paquet,cartes_pli), cartesIA) #cartes à redistribuer
    poids=np.zeros(len(cartes_possibles)) #matrice des poids de chaque cartes
    meneur=0# il s'agit du joueur qui mene.
    gagantPrecedent=0
    if len(cartes_pli)==0:
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            poids= jeuDeLaCarteMinimax(cartesIA,jeu1,jeu2,jeu3, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,meneur,gagantPrecedent)
    if len(cartes_pli)==1:
       for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            poids= jeuDeLaCarteMinimax(jeu1,cartesIA,jeu2,jeu3, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,meneur,gagantPrecedent) 
    if len(cartes_pli)==2:
       for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            poids= jeuDeLaCarteMinimax(jeu1,jeu2,cartesIA,jeu3, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,meneur,gagantPrecedent) 
    if len(cartes_pli)==3:
       for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            poids= jeuDeLaCarteMinimax(jeu1,jeu2,jeu3,cartesIA, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,meneur,gagantPrecedent) 
    return poids
        
        
    