# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:42:04 2019

@author: telmar
"""

def EncherePremierTour(jeu1, jeu2, jeu3, jeu4, carte):
    for i in range(4):
        res = input("Voulez-vous prendre ? (y/n)")
        if res == "y":
            return i, carte[1]
    return "Personne n'a pris"
