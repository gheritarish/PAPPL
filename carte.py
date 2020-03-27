import pygame
from pygame.locals import *
from tkinter import *
from PIL import Image, ImageTk


class Carte(Rect, object):

    def __init__(self, valeur, couleur):
        # Identité de la carte
        self.valeur = valeur
        self.couleur = couleur
        self.nom = valeur + couleur

        # Représentation graphique
        self.img_tk = Image.open("Ressources/Cartes/"+self.nom+".png")                  # Image pour Tkinter
        self.img_verticale = pygame.image.load("Ressources/Cartes/"+self.nom+".png")    # Image que l'on manipule lors du drag & drop
        self.angle = 0                                                                  # L'angle d'inclinaison de la carte
        self.img = self.img_verticale                                                   # Image pour Pygame (img_verticale tournée avec angle)
        self.msk = None                                                                 # Image avec prise en compte de la transparence (pour sélectionner plus finement avec la souris)
        
        # Informations sur l'état de la carte
        self.selected = False
        self.released = False
        self.jouee=False
    

    # Affiche le nom de la carte lors du print
    def __str__(self):
        return self.nom


    # Compare sa valeur avec celle d'une autre carte / permet de comparer la carte meneuse aux autres cartes
    def compare(self, carte, atout=False):
        # Si les cartes ne sont pas des figures, on les transforme en int pour les différencier
        try:
            valeur1 = int(self.valeur)
        except:
            valeur1 = self.valeur
        try:
            valeur2 = int(carte.valeur)
        except:
            valeur2 = carte.valeur

        # Cas 1: au début du jeu, pour décider qui commence
        # Cas 2: les deux cartes sont de la même couleur et aucune n'est un atout
        if atout==False or (self.couleur == carte.couleur and self.couleur != atout):        
            # Cas d'égalité
            if valeur1 == valeur2:
                return self

            # Si la carte est un As, elle gagne
            elif valeur1 == 1:
                return self
            elif valeur2 == 1:
                return carte

            # Si les deux cartes sont des numéros, on les compare facilement
            elif type(valeur1) == int and type(valeur2) == int:
                if valeur1 > valeur2:
                    return self
                else:
                    return carte

            # Si une carte est une figure et l'autre un numéro, la figure gagne
            elif type(valeur1) == str and type(valeur2) == int:
                return self
            elif type(valeur2) == str and type(valeur1) == int:
                return carte

            # Si les deux cartes sont des figures
            elif type(valeur2) == str and type(valeur1) == str:
                if (valeur1 == 'Valet'):
                    return carte
                elif (valeur1 == 'Roi'):
                    return self
                elif (valeur2 == 'Valet'):
                    return self
                elif (valeur2 == 'Roi'):
                    return carte
        
        # Si la carte meneuse est un atout et l'autre ne l'est pas
        elif self.couleur == atout and carte.couleur != atout: # Si la carte jouée est de l'atout
            return self

        # Si la carte meneuse n'est pas un atout et que l'autre l'est
        elif self.couleur!=atout and carte.couleur==atout:
            return carte  

        # Si les deux cartes sont des atouts 
        elif self.couleur==atout and carte.couleur==atout:
            if valeur1 == "Valet":
                return self
            elif valeur2 == "Valet":
                return carte
            elif valeur1 == 9:
                return self
            elif valeur2 == 9:
                return carte
            elif valeur1 == 1:
                return self
            elif valeur2 == 1:
                return carte
            elif valeur1 == 10:
                return self
            elif valeur2 == 10:
                return carte
            elif (type(valeur1) == int and type(valeur2) == int):
                if valeur1 > valeur2:
                    return self
                else:
                    return carte
            elif (type(valeur1) == str and type(valeur2) == int):
                return self
            elif (type(valeur1) == int and type(valeur2) == str):
                return carte
            elif (type(valeur1) == str and type(valeur2) == str):
                if (valeur1 == 'Roi'):
                    return self
                elif valeur1 == 'Dame':
                    return carte

        # La carte jouée n'est pas de la couleur de la carte meneuse
        else:
            return self


    # Positionne la carte pour Pygame: coordonnées égales à pos et tournée de angle.
    def positionne(self, angle, pos):
        self.angle = angle
        self.img = pygame.transform.rotate(self.img_verticale, self.angle)  # Image affichable (Surface)
        self.msk = pygame.mask.from_surface(self.img)                       # Image sans la partie transparence (Mask)
        Rect.__init__(self, self.img.get_rect(topleft=pos))                 # Image "sélectionnable" (Rect)


    # Prend en compte le drag & drop
    def update(self, ev):
        # Réinitialisation de l'état relachée
        if self.released:
            self.released = False

        # Sélection
        if ev.type == MOUSEBUTTONDOWN and ev.button == 1 and self.collidepoint(ev.pos):
            x, y = ev.pos
            self.selected = bool(self.msk.get_at((x-self.x, y-self.y)))

        # Relâche
        elif ev.type == MOUSEBUTTONUP and ev.button == 1 and self.collidepoint(ev.pos):
            self.selected = False
            self.released = True
            # Si la carte est positionnée au centre, elle est considérée comme jouée
            if self.x>440 and self.x<840 and self.y>205 and self.y<455:
                self.jouee=True

        # Mouvement de la carte avec la souris si sélectionnée
        elif ev.type == MOUSEMOTION and self.selected:
            relx, rely = ev.rel
            self.x += relx
            self.y += rely
            # L'image est verticale quand on la déplace
            self.img = self.img_verticale
