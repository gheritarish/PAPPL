# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:50:53 2019

@author: alepe
"""

from tkinter import *

def affichageOuiNon(string,a,b):
    fenetre = Tk()
    champ_label = Label(fenetre, text=string)
    champ_label.pack()
    var_choix = StringVar()
    choix = Radiobutton(fenetre, text=a, variable=var_choix, value=a)
    choix.pack() 
    choix = Radiobutton(fenetre, text=b, variable=var_choix, value=b)
    choix.pack()     
    fenetre.mainloop() 
    return(var_choix.get())
