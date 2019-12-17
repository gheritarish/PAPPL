# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:19:55 2019

@author: alepe
"""

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk

def affichageJeu(pli,jeu,meneur,couleurAtout,joueur,joueurs):
    Mafenetre = Tk()                
    Mafenetre.title("au tour de :"+joueur)
    Canevas = Canvas(Mafenetre) 
    Canevas.config(height=550,width=1400) 
    debutPli=475+(4-len(pli))*75
    if len(pli)>0:
        photo1 = ImageTk.PhotoImage(file=str(pli[0][0])+str(pli[0][1])+ ".PNG")
        Canevas.create_image(debutPli,150,image=photo1) 
        Canevas.pack() 
        Canevas.create_text(debutPli, 50,text=joueurs[0][0])
        Canevas.pack()
    if len(pli)>1:
        photo2 = ImageTk.PhotoImage(file=str(pli[1][0])+str(pli[1][1])+ ".PNG")                 
        Canevas.create_image(debutPli+150,150,image=photo2)           
        Canevas.pack()  
        Canevas.create_text(debutPli+150, 50,text=joueurs[1][0])
        Canevas.pack()
    if len(pli)>2:
        photo3 = ImageTk.PhotoImage(file=str(pli[2][0])+str(pli[2][1])+ ".PNG")                 
        Canevas.create_image(debutPli+300,150,image=photo3)           
        Canevas.pack()  
        Canevas.create_text(debutPli+300, 50,text=joueurs[2][0])
        Canevas.pack()
    L=[]
    debut = 175+(8-len(jeu))*75
    if meneur != 4 :
        Canevas.create_text(700, 275,text="la couleur d'atout est "+couleurAtout+ ", le meneur est "+ joueurs[meneur][0] +" et votre jeu est:")
    else :
        Canevas.create_text(700, 275,text="la couleur d'atout est "+couleurAtout+ " et votre jeu est:")
    Canevas.pack()  
    for i in range(len(jeu)):
        L.append(ImageTk.PhotoImage(file=str(jeu[i][0])+ str(jeu[i][1]) + ".PNG"))                
        Canevas.create_image(debut +i*150,400,image=L[i])           
        Canevas.pack()  
        Canevas.create_text(debut +i*150,500,text=(i+1))          
        Canevas.pack()      
    
    var_choix = StringVar()
    for i in range(len(jeu)):
        choix = Radiobutton(Mafenetre, text=(i+1), variable=var_choix, value=(i+1))
        choix.pack() 
        
    Bouton1 = Button(Mafenetre, text = 'OK', command = Mafenetre.destroy)
    Bouton1.pack()
    Mafenetre.mainloop() 
    return(var_choix.get())
pli=['1pique.PNG','1trèfle.PNG','1coeur.PNG']
jeu=['1pique.PNG','1trèfle.PNG','1coeur.PNG','1carreau.PNG','1pique.PNG','1trèfle.PNG','1coeur.PNG']
couleurAtout='coeur'
joueur='fred'
joueurs=['roger','bernadette','gerard','fred']
meneur='roger'

