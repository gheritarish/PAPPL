# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:36:08 2019

@author: alepe
"""
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk


def affichageDistribution(jeu,carte,joueur,tour):
    Mafenetre = Tk()
    champ_label = Label(Mafenetre, text="Nous sommes au tour "+str(tour)+", "+joueur+" que voulez-vous faire?")
    champ_label.pack()
    Canevas = Canvas(Mafenetre) 
    Canevas.config(height=550,width=1400) 
    photo1 = ImageTk.PhotoImage(file=carte)
    Canevas.create_image(700,150,image=photo1) 
    Canevas.pack()
    debut=175+(8-len(jeu))*75
    L=[]
    for i in range(len(jeu)):
        L.append(ImageTk.PhotoImage(file=jeu[i]))                
        Canevas.create_image(debut +i*150,400,image=L[i])           
        Canevas.pack()  
        Canevas.create_text(debut +i*150,500,text=i)          
        Canevas.pack()  
    champ_label = Label(Mafenetre, text=joueur+", voulez-vous prendre?")
    champ_label.pack()
    var_choix = StringVar()
    choix = Radiobutton(Mafenetre, text="yes", variable=var_choix, value="y")
    choix.pack() 
    choix = Radiobutton(Mafenetre, text="no", variable=var_choix, value="n")
    choix.pack()     
    Mafenetre.mainloop() 
    return(var_choix.get())
jeu=['1pique.PNG','1trèfle.PNG','1coeur.PNG','1carreau.PNG','1pique.PNG','1trèfle.PNG','1coeur.PNG']
carte='1pique.PNG'
tour=1
joueur='roger'

