# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:21:43 2019

@author: alepe
"""

from tkinter import *
def affichageTexte(string):
    fenetre = Tk()
    champ_label = Label(fenetre, text=string)
    champ_label.pack()
    Bouton1 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
    Bouton1.pack()
    fenetre.mainloop() 