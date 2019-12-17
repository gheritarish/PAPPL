# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:39:54 2019

@author: alepe
"""

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk



def affichagePli(pli,joueur,gagnant):
    Mafenetre = Tk()                
    Mafenetre.title("Plis réalisé")
    Canevas = Canvas(Mafenetre) 
    photo1 = ImageTk.PhotoImage(file=str(pli[0][0])+str(pli[0][1])+ ".PNG")       

    Canevas.config(height=650,width=1400) 
    Canevas.create_image(475,150,image=photo1)          
    Canevas.pack()   

    photo2 = ImageTk.PhotoImage(file=str(pli[1][0])+str(pli[1][1])+ ".PNG")                 
    Canevas.create_image(625,150,image=photo2)           
    Canevas.pack()  
    
    photo3 = ImageTk.PhotoImage(file=str(pli[2][0])+str(pli[2][1])+ ".PNG")                 
    Canevas.create_image(775,150,image=photo3)           
    Canevas.pack()  
    
    photo4 = ImageTk.PhotoImage(file=str(pli[3][0])+str(pli[3][1])+ ".PNG")                 
    Canevas.create_image(925,150,image=photo4)           
    Canevas.pack()  

    Canevas.create_text(700, 300,text="Le joueur " + gagnant + " remport le pli")
    Canevas.pack()
    
    Canevas.create_text(475, 50,text=joueur[0][0])
    Canevas.pack()
    
    Canevas.create_text(625, 50,text=joueur[1][0])
    Canevas.pack()
    
    Canevas.create_text(775, 50,text=joueur[2][0])
    Canevas.pack()
    
    Canevas.create_text(925, 50,text=joueur[3][0])
    Canevas.pack()

    Bouton1 = Button(Mafenetre, text = 'OK', command = Mafenetre.destroy)
    Bouton1.pack()    
    
    Mafenetre.mainloop() 
    

    
p=['1pique.PNG','1trèfle.PNG','1coeur.PNG','1carreau.PNG']

joueurs=['roger','riger','celine','romane']
gagant='roger'