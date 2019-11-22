# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:50:24 2019

@author: alepe
"""

def creationPaquetDeCartes():
    valeur = [1,7,8,9,10,'Valet','Dame','Roi']
    couleur = ['pique','coeur','trèfle','carreau']
    paquet = []
    for i in range(len(couleur)):
        for j in range(len(valeur)):
            paquet.append([valeur[j],couleur[i]])
    return (paquet)
