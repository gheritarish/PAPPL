import math
from carte import Carte
import pygame
from pygame.locals import *


class Joueur():

    def __init__(self, nom, type, equipe):
        self.nom = nom
        self.type = type
        self.equipe = equipe
        self.cartes = []
        self.preneur = False
        self.ordre=None


    def __str__(self):
        return self.nom


    def pioche(self, paquet, nb):
        for _ in range(nb):
            self.cartes.append(paquet.cartes.pop())


    def peut_jouer(self, carte, tour, atout, joueurs, interface):
        """if carte.nom=="Roi"+atout or carte.nom=="Reine"+atout:
            interface.demande_belote=True"""
            
        if len(tour.pli)==0:
            return True
        elif carte.couleur != tour.pli[0].couleur:
            for carte_joueur in self.cartes:
                if carte_joueur.couleur == tour.pli[0].couleur:
                    return False
        if carte.couleur==atout:
            for carte_pli in tour.pli:
                if carte_pli.couleur==atout and carte.nom!=carte.compare(carte_pli, atout).nom:
                    for carte_joueur in self.cartes:
                        if carte_joueur.couleur==atout and carte_joueur.nom==carte_joueur.compare(carte_pli, atout).nom:
                            return False
        elif joueurs[tour.id_maitre].equipe!=self.equipe:
            for carte_joueur in self.cartes:
                if carte_joueur.couleur==atout:
                    return False
        return True



    def jouer(self, interface, joueurs, tour, atout):
        joue = True
        while joue:
            interface.affichage(self.cartes)
            for event in pygame.event.get():
                if event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION):
                    for pos, carte in enumerate(self.cartes):
                        carte.update(event)
                        if carte.jouee:
                            if self.peut_jouer(carte, tour, atout, joueurs, interface):
                                self.cartes.remove(carte)
                                return carte
                            else:
                                carte.jouee=False
                                interface.positionne_cartes(self)


