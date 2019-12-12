# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:39:41 2019

@author: alepe
"""
from MelangeCarte import melangeCarte

def redistributionIA(cartesAutreJoueur,position):
    cartesMelange=melangeCarte(cartesAutreJoueur)
    jeu1=[]
    jeu2=[]
    jeu3=[]
    if position == 0 or position == 3:
        jeu1=cartesMelange[0:len(cartesMelange)//3]
        jeu2=cartesMelange[len(cartesMelange)//3:2*len(cartesMelange)//3]
        jeu3=cartesMelange[len(2*cartesMelange)//3:3*len(cartesMelange)//3]
    if position==1:
        for i in range(len(cartesMelange)):
            if i<=(len(cartesMelange)+1)//3-2 :
                jeu1.append(cartesMelange[i])
            if i> (len(cartesMelange)+1)//3-2 and i <= 2*(len(cartesMelange)+1)//3-2:
                jeu2.append(cartesMelange[i])
            if i> 2*(len(cartesMelange)+1)//3-2 and i<= 3*(len(cartesMelange)+1)//3-2:
                jeu3.append(cartesMelange[i])
    if position ==2:
        for i in range(len(cartesMelange)):
            if i<=(len(cartesMelange)+2)//3-2 :
                jeu1.append(cartesMelange[i])
            if i> (len(cartesMelange)+2)//3-2 and i <= 2*(len(cartesMelange)+2)//3-3:
                jeu2.append(cartesMelange[i])
            if i> 2*(len(cartesMelange)+2)//3-3 and i<= 3*(len(cartesMelange)+2)//3-3:
                jeu3.append(cartesMelange[i])
    
    return jeu1,jeu2,jeu3