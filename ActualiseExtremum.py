# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:05:53 2020

@author: Jérôme VILLEROT
"""
"""
Cette fonction 
"""

def actualise(position_joueur,positionIA,valeur_noeud,valeur_branche):
    if (valeur_noeud == None):
        return valeur_branche
    estAvecIA = ((((positionIA - position_joueur)%4)%2) == 0)
    if (estAvecIA):
        return (max(valeur_noeud, valeur_branche))
    else:
        return (min(valeur_noeud, valeur_branche))