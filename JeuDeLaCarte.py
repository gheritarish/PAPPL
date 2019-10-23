# -*- coding=utf-8 -*-
"""
Created on Tue Oct 22 17.13.30

@author: telmar
"""
<<<<<<< HEAD

def JeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout):
    """Le joueur 4 n'existe pas. Belote reste à joueur 4 si personne ne l'a"""
    belote = 4
    gagant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    for i in range(8):
        gagnant, pli, jeu1, jeu2, jeu3, jeu4 = Pli(jeu1, jeu2, jeu3, jeu4, gagant_prec, belote, atout)
        gagnant_prec = gagnant
        if gagant in [0,2]:
            plis_equipe1.append(pli)
        else:
            plis_equipe2.append(pli)
    return plis_equipe1, plis_equipe2, gagant, belote
=======
from Pli import pli
def jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout):
    """Le joueur 4 n'existe pas. Belote reste à joueur 4 si personne ne l'a"""
    belote = 4
    gagnant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    for i in range(8):
        jeu1, jeu2, jeu3, jeu4,gagnant, plis,belote = pli(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote, atout)
        gagnant_prec = gagnant
        if gagnant in [0,2]:
            plis_equipe1.append(plis)
        else:
            plis_equipe2.append(plis)
    return plis_equipe1, plis_equipe2, gagnant, belote
>>>>>>> alexandre
