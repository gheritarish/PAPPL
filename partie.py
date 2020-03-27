import random
from tkinter import *
from PIL import Image, ImageTk
import pygame
from pygame.locals import *
from carte import Carte
from paquet import Paquet
from joueur import Joueur
from interface import Interface


class Partie:

    def __init__(self, type=None, max=None, difficulte=None, joueurs=None):
        self.type = type
        self.max = max
        self.difficulte = difficulte
        self.joueurs = joueurs

    def continuer(self, equipe1, equipe2):
        # CONDITION DE FIN DE PARTIE
        if self.type=="Points":
            if self.max<equipe1.score or self.max<equipe2.score:
                return False
        elif self.type=="Tours":
            self.max-=1
            if self.max==0:
                return False
        return True

    def premier_joueur(self, paquet):
        # FENETRE
        fenetre = Tk()
        fenetre.iconbitmap("Ressources/logo.png")
        fenetre.title("Choix du premier joueur")
        fenetre.geometry("1280x720+0+0")

        # EQUIPE 1
        equipe1_frame = LabelFrame(fenetre, text="Equipe 1")
        equipe1_frame.pack()

        # EQUIPE 2
        equipe2_frame = LabelFrame(fenetre, text="Equipe 2")
        equipe2_frame.pack()

        # ON PIOCHE TANT QU'IL Y A EGALITE
        egalite = True
        while egalite:
            # CHAQUE JOUEUR PIOCHE UNE CARTE
            cartes_piochees=[]
            for joueur in self.joueurs:
                joueur.pioche(paquet, 1)
                cartes_piochees.append(joueur.cartes.pop())

            # ON COMPARE LES CARTES ENTRE ELLES
            max=cartes_piochees[0]
            for carte in cartes_piochees:
                max=max.compare(carte)

            # VERIFICATION D'UN MAXIMUM UNIQUE
            egalite=False
            for i in range(4):
                if max.nom==cartes_piochees[i].nom:
                    id_max=i
                elif max.valeur==cartes_piochees[i].valeur:
                    egalite=True

        # IMAGES DES CARTES
        for i, carte in enumerate(cartes_piochees):
            if i == 0:
                img_tk11 = ImageTk.PhotoImage(carte.img_tk)
                image11 = Label(equipe1_frame, image=img_tk11, text=joueur.nom)
                image11.pack(side=LEFT)
            if i == 1:
                img_tk21 = ImageTk.PhotoImage(carte.img_tk)
                image21 = Label(equipe2_frame, image=img_tk21, text=joueur.nom)
                image21.pack(side=LEFT)
            if i == 2:
                img_tk12 = ImageTk.PhotoImage(carte.img_tk)
                image12 = Label(equipe1_frame, image=img_tk12, text=joueur.nom)
                image12.pack(side=RIGHT)
            if i == 3:
                img_tk22 = ImageTk.PhotoImage(carte.img_tk)
                image22 = Label(equipe2_frame, image=img_tk22, text=joueur.nom)
                image22.pack(side=RIGHT)

        # PREMIER JOUEUR
        premier_joueur = self.joueurs[id_max]
        text = Label(fenetre, text=premier_joueur.nom+" distribue les cartes.")
        text.pack()

        # CHANGEMENT DE L'ordre_joueur
        self.ordre_joueurs((id_max+1)%4)

        # BOUTON OK
        def quitter():
            fenetre.destroy()
        ok = Button(fenetre, text="OK", command=quitter)
        ok.pack()

        # MAINLOOP
        fenetre.mainloop()

    def ordre_joueurs(self, id_premier):
        self.joueurs= [self.joueurs[id_premier], self.joueurs[(id_premier+1)%4], self.joueurs[(id_premier+2)%4], self.joueurs[(id_premier+3)%4]]
        for i, joueur in enumerate(self.joueurs):
            joueur.ordre=i