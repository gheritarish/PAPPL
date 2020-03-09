# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:17:39 2020

@author: Jérôme VILLEROT
"""

def laBorne(alpha, beta, position_joueur, positionIA):
    if ((((positionIA - position_joueur)%4)%2) == 0):
        return alpha
    else:
        return beta