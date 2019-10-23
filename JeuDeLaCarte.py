# -*- coding=utf-8 -*-
"""
Created on Tue Oct 22 17.13.30

@author: telmar
"""
from Pli import pli
def jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout):
    """Le joueur 4 n'existe pas. Belote reste à joueur 4 si personne ne l'a"""
    belote = 4
    rebelote=4
    gagnant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    for i in range(8):
        jeu1, jeu2, jeu3, jeu4,gagnant, plis,belote,rebelote = pli(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote,rebelote, atout)
        gagnant_prec = gagnant
        if gagnant in [0,2]:
            plis_equipe1.append(plis)
        else:
            plis_equipe2.append(plis)
    return plis_equipe1, plis_equipe2, gagnant, rebelote
