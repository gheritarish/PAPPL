# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:43:26 2019

@author: alepe
"""
######################################
# Importation des modules nécessaires:
######################################


from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk


####################################
# Creation de la fenetre principale:
####################################


Mafenetre = Tk()                
Mafenetre.title("Image")                                  # Titre de la fenetre


######################################################################
# Creation d'un widget Canvas pour afficher une image dans la fenetre:
######################################################################

Canevas = Canvas(Mafenetre)              


###################################################
# Importation de l'image avec un boite de dialogue:
###################################################


#filename = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('jpg files','.jpg'),('bmp files','.bmp'),('all files','.*')]) 


#######################
# Affichage de l'image:
#######################


photo = ImageTk.PhotoImage(file='1pique.PNG')                  # Nécessaire pour travailler avec différents types d'images

Canevas.config(height=650,width=1400)  # Règle la taille du canvas par rapport à la taille de l'image 
Canevas.create_image(150,150,image=photo)            # Règle l'emplacement du milieu de l'image, ici dans le coin Nord Ouest (NW) de la fenetre  
Canevas.pack()   

photo1 = ImageTk.PhotoImage(file='1trefle.PNG')                  # Nécessaire pour travailler avec différents types d'images


Canevas.create_image(300,150,image=photo1)            # Règle l'emplacement du milieu de l'image, ici dans le coin Nord Ouest (NW) de la fenetre  
Canevas.pack()  

Canevas.create_text(700, 10,text="Pli réalisé")
Canevas.pack()




Mafenetre.mainloop()  