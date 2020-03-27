import pygame
from pygame.locals import *

class Manche():

    def __init__(self, score_additionnel):
        self.enchere=True
        self.preneur=""
        self.atout=""
        self.preneur=0
        self.score_additionnel=score_additionnel


    def encherir(self, joueurs, interface, retourne, deuxieme=False):
        for joueur in joueurs:
            interface.positionne_noms(joueurs, joueur)
            interface.positionne_cartes(joueur)
            choix = ""
            while choix == "":
                interface.affichage(joueur.cartes, True, retourne)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        interface.fenetre=pygame.display.quit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        interface.fenetre=pygame.display.quit()
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if interface.prendre_rect.collidepoint(event.pos):
                            choix = "Prendre"
                        if interface.passer_rect.collidepoint(event.pos):
                            choix = "Passer"
            if choix == "Prendre":
                self.enchere = False
                joueur.cartes.append(retourne)
                if deuxieme == True:
                    clic = False
                    while not clic:
                        interface.affichage(joueur.cartes)
                        for event in pygame.event.get():
                            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                                if interface.trefle_rect.collidepoint(event.pos):
                                    clic = True
                                    self.atout = "trèfle"
                                if interface.pique_rect.collidepoint(event.pos):
                                    clic = True
                                    self.atout = "pique"
                                if interface.coeur_rect.collidepoint(event.pos):
                                    clic = True
                                    self.atout = "coeur"
                                if interface.carreau_rect.collidepoint(event.pos):
                                    clic = True
                                    self.atout = "carreau"
                                    interface.montrer_atout(self.atout)
                else:
                    self.atout = retourne.couleur
                joueur.preneur=True
                self.preneur = joueur.equipe
                break

    def resultat(self, equipe1, equipe2):
        if self.preneur == 1:
            equipe2.score+=equipe2.score_manche
            if equipe1.score_manche>=82:
                equipe1.score+=equipe1.score_manche
            elif equipe1.score_manche==equipe2.score_manche:
                return equipe1.score_manche
        elif self.preneur==2:
            equipe1.score+=equipe1.score_manche
            if equipe2.score_manche>=82:
                equipe2.score+=equipe2.score_manche
            elif equipe2.score_manche==equipe1.score_manche:
                return equipe2.score_manche
        return 0
        

    