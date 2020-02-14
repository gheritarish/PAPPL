# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:34:38 2019

@author: clegui
"""

def cartestombees(cartes_tombees, pli):
    """Fonction qui prend en mémoire les cartes tombées à partir du pli réalisé et des cartes déjà tombées."""
    for carte in pli:
        cartes_tombees.append(carte)
    return cartes_tombees
    


