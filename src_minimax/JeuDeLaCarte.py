# -*- coding=utf-8 -*-
"""
Created on Tue Oct 22 17:13:30 2019

@author: telmar
"""
from PliIA import pliIA
from CreationPaquetDeCartes import creationPaquetDeCartes

def jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout,joueur):
    """Le joueur 4 n'existe pas. Belote reste à joueur 4 si personne ne l'a"""
    belote = 4
    rebelote=4
    gagnant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    cartes_restantes = creationPaquetDeCartes()
    numero_pli=0
    for i in range(8):
        jeu1, jeu2, jeu3, jeu4,gagnant, plis,belote,rebelote = pliIA(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote,rebelote, atout,joueur,numero_pli)
        gagnant_prec = gagnant
        if gagnant in [0,2]:
            plis_equipe1.append(plis)
        else:
            plis_equipe2.append(plis)
        numero_pli=numero_pli+1
        cartes_restantes = suppressionCartes(cartes_restantes, plis)

    return plis_equipe1, plis_equipe2, gagnant, rebelote
