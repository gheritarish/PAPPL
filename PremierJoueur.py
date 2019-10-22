# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:45:09 2019

@author: alepe
"""
import CompareCarte

import random
def PremierJoueur(nom1,nom2,paquet):
    condition =0
    while condition==0:
        j1=random.randint(0,31)
        j2=random.randint(0,31)
        if j1 !=j2:
            condition = CompareCarte(paquet[j1], paquet[j2])
    if condition == 1:
        return (nom1, paquet[j1], paquet[j2])
    else :
        return (nom2, paquet[j1], paquet[j2])
    
    
    
