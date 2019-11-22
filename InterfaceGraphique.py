# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:07:26 2019

@author: alepe
"""
"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()
#un bouton
#bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
#bouton_quitter.pack()


#écrire dans la fenetre
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=1)
ligne_texte.pack()
#cocher une case

var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

liste = Listbox(fenetre)
liste.pack()
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

var_case.get() #1 ou 0 suivant qu'on ait coché la case ou non

print(liste.curselection())