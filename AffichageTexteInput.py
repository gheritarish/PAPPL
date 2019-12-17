# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:44:26 2019

@author: alepe
"""

from tkinter import *
def affichageTexteInput(string):
    fenetre = Tk()
    champ_label = Label(fenetre, text=string)
    champ_label.pack()
    var_texte = StringVar()
    ligne_texte = Entry(fenetre, textvariable=var_texte, width=50)
    ligne_texte.pack() 
    Bouton1 = Button(fenetre, text = 'OK', command = fenetre.destroy)
    Bouton1.pack()
    fenetre.mainloop()
    return var_texte.get()