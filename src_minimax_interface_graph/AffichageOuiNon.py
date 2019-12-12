# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:50:53 2019

@author: alepe
"""

from tkinter import *
def affichageOuiNon(string,liste):
    fenetre = Tk()
    champ_label = Label(fenetre, text=string)
    champ_label.pack()
    var_choix = StringVar()
    for i in range(len(liste)):
        choix = Radiobutton(fenetre, text=liste[i], variable=var_choix, value=liste[i])
        choix.pack()  
    Bouton1 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
    Bouton1.pack()
    fenetre.mainloop() 
    return(var_choix.get())
