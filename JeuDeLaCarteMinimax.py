# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:12:25 2019

@author: alepe
"""
from CartesJouables import cartesJouables

def jeuDeLaCarteMinimax(cartesIA,jeu1,jeu2,jeu3, paquet,couleur_atout,carte_meneuse, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,meneur):
    cartes_possibles=cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse)
    if num_pli==7 and len(cartes_pli)==4: #condition d'arret, on est au dernier pli et la derniere carte est jouée
        if meneur in [0,2]:
            plis_equipe1.append(cartes_pli)
        else:
            plis_equipe2.append(cartes_pli)
        #il reste à calculer les scores et à update les poids ave le score
        