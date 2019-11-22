# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:48:13 2019

@author: alepe
"""

def ordreJoueur(premier_joueur,joueur):
    if joueur[0]==premier_joueur :
        ordre=[joueur[1],joueur[2],joueur[3],joueur[0]]
    elif joueur[1]==premier_joueur :
        ordre=[joueur[2],joueur[3],joueur[0],joueur[1]]
    elif joueur[2]==premier_joueur :
        ordre=[joueur[3],joueur[0],joueur[1],joueur[2]]
    elif joueur[3]==premier_joueur :
        ordre=[joueur[0],joueur[1],joueur[2],joueur[3]]
    return ordre
