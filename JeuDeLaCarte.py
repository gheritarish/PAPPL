# -*- coding=utf-8 -*-
"""
Created on Tue Oct 22 17.13.30

@author: telmar
"""

def JeuDeLaCarte(jeu1, jeu2, jeu3, jeu4):
    """Le joueur 4 n'existe pas. Belote reste à joueur 4 si personne ne l'a"""
    belote = 4
    gagant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    for i in range(8):
        gagnant, pli, jeu1, jeu2, jeu3, jeu4 = Pli(jeu1, jeu2, jeu3, jeu4, gagant_prec, belote)
        gagnant_prec = gagnant
        if gagant in [0,2]:
            plis_equipe1.append(pli)
        else:
            plis_equipe2.append(pli)
    return plis_equipe1, plis_equipe2, gagant, belote
