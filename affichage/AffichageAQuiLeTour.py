# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:50:08 2019

@author: alepe
"""
from tkinter import *
def affichageAQuiLeTour(joueur): #on rentre le nom du joueur qui doit jouer, le but est de faire une coupure d'écran entre chaque joueur pour pas que l'on voit le jeu de nos adversaires
    
    fenetre = Tk()
    champ_label = Label(fenetre, text="c'est au tour de "+joueur)
    champ_label.pack()
    fenetre.mainloop() 
joueur='roger'