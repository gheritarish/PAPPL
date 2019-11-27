# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:31:29 2019

@author: alepe
"""
from CartesJouables import cartesJouables
from SuppressionCartes import suppressionCartes
from RedistributionIA import redistributionIA
from numpy import np
from JeuDeLaCarteMinimaxInitiale import jeuDeLaCarteMinimaxInitiale

#carte restante qui est update à chaque plis
def minimax(cartesIA, paquet,couleur_atout,carte_meneuse,meneur, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli):
    cartes_possibles=cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse) # on recupère les cartes jouables
    cartesAutreJoueur=suppressionCartes(suppressionCartes(paquet,cartes_pli), cartesIA) #cartes à redistribuer
    poids=np.zeros(len(cartes_possibles)) #matrice des poids de chaque cartes
    if len(cartes_pli)==0:
        positionIA=0
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitiale(cartesIA,jeu1,jeu2,jeu3, paquet,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur)
    if len(cartes_pli)==1:
        positionIA=1
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitiale(jeu1,cartesIA,jeu2,jeu3, paquet,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur) 
    if len(cartes_pli)==2:
        positionIA=2
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitiale(jeu1,jeu2,cartesIA,jeu3, paquet,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur) 
    if len(cartes_pli)==3:
        positionIA=3
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitiale(jeu1,jeu2,jeu3,cartesIA, paquet,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur) 
    
    return poids
        
        
    