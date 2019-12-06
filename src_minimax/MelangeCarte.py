# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:46:11 2019

@author: alepe
"""
import random

def melangeCarte(paquet):
    """Fonction qui permet de mélanger un paquet non-mélangé"""
    nouveau_paquet = []
    for i in range(len(paquet)):
        nouveau_paquet.append(paquet[random.randint(0,31-i)])
        paquet.remove(nouveau_paquet[-1])
    return nouveau_paquet

    
