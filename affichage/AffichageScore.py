# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:04:25 2019

@author: alepe
"""

"""
param : 
score1=entier (score de l'équipe 1)
score2=entier (score de l'équipe 2)
partie = Char (type de partie)
fin= entier (0 ou 1) correspond au fait qu'on soit ou non à la fin de la partie
maximum : entier . Si c'est une partie au score elle contient de le score max, sinon elle contient le tour où nous sommes
"""
from tkinter import *
def affichageScore(score1,score2,partie,maximum,fin):
    fenetre = Tk()
    if partie=="p":
        if fin==1:
            champ_label = Label(fenetre, text="fin de la partie, le score de "+str(maximum)+" a été atteint")
            champ_label.pack()
        champ_label = Label(fenetre, text="le score de l'équipe 1 est de "+str(score1))
        champ_label.pack()
        champ_label = Label(fenetre, text="le score de l'équipe 2 est de "+str(score2))
        champ_label.pack()
    elif partie=="t":
        if fin==1:
            champ_label = Label(fenetre, text="fin de la partie, nous sommes arrivé au tour "+str(maximum))
            champ_label.pack()
        else :
            champ_label = Label(fenetre, text="nous sommes au tour "+str(maximum))
            champ_label.pack()            
        champ_label = Label(fenetre, text="le score de l'équipe 1 est de "+str(score1))
        champ_label.pack()
        champ_label = Label(fenetre, text="le score de l'équipe 2 est de "+str(score2))
        champ_label.pack()  
    fenetre.mainloop() 
        
score1=1000
score2=120
partie="t"
maximum=2000
fin=0