# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:52:54 2020

@author: PM, clegui
"""
import csv

def enregistre(jeu,p1, p2, w, pre, po1, po2,couleur):
    
    listeNB = jeu + [str(p1[0]), str(p1[1]), str(p2[0]), str(p2[1]), str(w), str(pre), str(po1), str(po2), str(couleur)]
    with open('resultats_entrainement_ann_test.csv', 'a', newline='') as f:
        writer = csv.writer(f).writerow(listeNB)
