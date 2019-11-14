# -*- coding=utf-8 -*-
"""
Created on Wed Nov 13 16:00:45 2019

@author: telmar
"""

def probabilites(carte, cartes, atout):
    """Prend en argument la carte dont on veut calculer la probabilité d'être maîtresse, les cartes que l'on n'a pas qui n'ont pas encore été jouées et l'atout"""
    plus_fortes = 0
    plus_faibles = 0
    for card in cartes:
        if compareCarteJeu(card, carte, atout) == 1:
            plus_fortes += 1
        elif compareCarteJeu(card, carte, atout) == -1:
            plus_faibles += 1
    return plus_faibles / (plus_fortes + plus_faibles)

