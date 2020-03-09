# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:46:00 2020

@author: Jérôme VILLEROT
"""

def miseAJourAB(valeur, alpha, beta, position_joueur, positionIA):
    if (valeur != None):   
        if ((((positionIA - position_joueur)%4)%2) == 0):
            alpha = max(alpha, valeur)
        else:
            beta = min(beta, valeur)
    return alpha, beta
            