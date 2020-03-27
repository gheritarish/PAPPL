import pygame
from pygame.locals import *
from carte import Carte
import math

class Interface():

    def __init__(self, joueurs):
        pygame.init()

        logo = pygame.image.load("Ressources/logo.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Jeu de belote")
        self.fenetre = pygame.display.set_mode((1280, 720), FULLSCREEN)

        self.fond = pygame.image.load("Ressources/background2.jpg")
        self.border = pygame.image.load("Ressources/border.png").convert_alpha()
        self.face = pygame.image.load("Ressources/face.png").convert_alpha()
        self.gauche = pygame.image.load("Ressources/gauche.png").convert_alpha()
        self.droite = pygame.image.load("Ressources/droite.png").convert_alpha()
        self.prendre_img = pygame.image.load("Ressources/prendre.png").convert_alpha()
        self.prendre_rect= self.prendre_img.get_rect(topleft=(690, 285))
        self.passer_img = pygame.image.load("Ressources/passer.png").convert_alpha()
        self.passer_rect=self.passer_img.get_rect(topleft=(690, 385))
        self.trefle_img=pygame.image.load("Ressources/trefle.png").convert_alpha()
        self.trefle_rect=self.trefle_img.get_rect(topleft=(380, 145))
        self.coeur_img=pygame.image.load("Ressources/coeur.png").convert_alpha()
        self.coeur_rect=self.coeur_img.get_rect(topleft=(850, 145))
        self.carreau_img=pygame.image.load("Ressources/carreau.png").convert_alpha()
        self.carreau_rect=self.carreau_img.get_rect(topleft=(380, 465))
        self.pique_img=pygame.image.load("Ressources/pique.png").convert_alpha()
        self.pique_rect=self.pique_img.get_rect(topleft=(850,465))

        self.font = pygame.font.Font(None, 32)
        self.text0 = self.font.render(joueurs[0].nom, True, (252,252,252), (0,200,0))
        self.text0_rect = self.text0.get_rect()
        self.text1 = self.font.render(joueurs[1].nom, True, (252,252,252), (0,200,0))
        self.text1_rect = self.text1.get_rect()
        self.text2 = self.font.render(joueurs[2].nom, True, (252,252,252), (0,200,0))
        self.text2_rect = self.text2.get_rect()
        self.text3 = self.font.render(joueurs[3].nom, True, (252,252,252), (0,200,0))
        self.text3_rect = self.text3.get_rect()


    def montrer_atout(self, atout):
        if atout=="trèfle":
            self.trefle_img=pygame.image.load("Ressources/trefle_atout.png").convert_alpha()
            self.trefle_rect=self.trefle_img.get_rect(topleft=(380, 145))
        elif atout=="coeur":
            self.coeur_img=pygame.image.load("Ressources/coeur_atout.png").convert_alpha()
            self.coeur_rect=self.coeur_img.get_rect(topleft=(850, 145))
        elif atout=="carreau":
            self.carreau_img=pygame.image.load("Ressources/carreau_atout.png").convert_alpha()
            self.carreau_rect=self.carreau_img.get_rect(topleft=(380, 465))
        elif atout=="pique":
            self.pique_img=pygame.image.load("Ressources/pique_atout.png").convert_alpha()
            self.pique_rect=self.pique_img.get_rect(topleft=(850,465))


    def positionne_noms(self, joueurs, joueur):
        self.text0 = self.font.render(joueur.nom, True, (252,252,252), (0,200,0))
        self.text0_rect = self.text0.get_rect(center=(640,670))
        self.text1 = self.font.render(joueurs[(joueur.ordre+1)%4].nom, True, (252,252,252), (0,200,0))
        self.text1_rect = self.text1.get_rect(center=(1180,360))
        self.text2 = self.font.render(joueurs[(joueur.ordre+2)%4].nom, True, (252,252,252), (0,200,0))
        self.text2_rect = self.text2.get_rect(center=(640,50))
        self.text3 = self.font.render(joueurs[(joueur.ordre+3)%4].nom, True, (252,252,252), (0,200,0))
        self.text3_rect = self.text3.get_rect(center=(100,360))


    def positionne_cartes(self, joueur):
        nb = len(joueur.cartes)
        rayon = 300*nb
        espace = 10
        alpha = math.asin(58/rayon)
        beta = math.asin(espace/2/rayon)
        gamma = alpha+beta
        if nb % 2:
            milieu = int(nb/2-0.5)
            x1 = 582
            x2 = x1
            y = 500
            joueur.cartes[milieu].positionne(0, (x1, y))
            angle = 2*gamma
            for i in range(milieu):
                dx1 = espace*math.cos(gamma+2*i*gamma) + \
                    116*math.cos(2*(i+1)*gamma)
                dx2 = espace*math.cos(gamma+2*i*gamma)+116*math.cos(2*i*gamma)
                dy = espace*math.sin(gamma+2*i*gamma)+116*math.sin(2*i*gamma)

                x1 -= dx1
                x2 += dx2
                y += dy

                joueur.cartes[milieu-i -
                            1].positionne(math.degrees(angle), (x1, y))
                joueur.cartes[milieu+i +
                            1].positionne(math.degrees(-angle), (x2-166*math.sin(angle), y))
                angle += 2*(alpha+beta)
        else:
            centre2 = int(nb/2)
            centre1 = centre2-1
            dx = 116*math.cos((alpha+beta))
            x1 = 635-dx
            x2 = 645
            y = 500
            angle = gamma
            joueur.cartes[centre1].positionne(angle, (x1, y))
            joueur.cartes[centre2].positionne(-angle, (x2, y))
            for i in range(centre1):
                dx1 = espace*math.cos(2*(i+1)*gamma) + \
                    116*math.cos(gamma+2*(i+1)*gamma)
                dx2 = espace*math.cos(2*i*gamma)+116*math.cos(gamma+2*i*gamma)
                dy2 = espace*math.sin(2*(i+1)*gamma) + \
                    116*math.sin(gamma+2*i*gamma)
                x1 -= dx1
                x2 += dx2
                y += dy2
                joueur.cartes[centre1-i -
                            1].positionne(math.degrees(angle), (x1, y))
                joueur.cartes[centre2+i +
                            1].positionne(math.degrees(-angle), (x2-166*math.sin(angle), y))
                angle += 2*gamma


    def affichage(self, cartes, enchere=False, retourne=None):
        self.fenetre.blit(self.fond, (0, 0))
        self.fenetre.blit(self.border, (390, 155))
        self.fenetre.blit(self.face, (540, 20))
        self.fenetre.blit(self.gauche, (-20, 210))
        self.fenetre.blit(self.droite, (1010, 210))
        self.fenetre.blit(self.trefle_img, self.trefle_rect.topleft)
        self.fenetre.blit(self.coeur_img, self.coeur_rect.topleft)
        self.fenetre.blit(self.carreau_img, self.carreau_rect.topleft)
        self.fenetre.blit(self.pique_img, self.pique_rect.topleft)
        self.fenetre.blit(self.text0, self.text0_rect.center)
        self.fenetre.blit(self.text1, self.text1_rect.center)
        self.fenetre.blit(self.text2, self.text2_rect.center)
        self.fenetre.blit(self.text3, self.text3_rect.center)
        for carte in cartes:
            self.fenetre.blit(carte.img, carte.topleft)
        if enchere:
            self.fenetre.blit(self.prendre_img, (690, 285))
            self.fenetre.blit(self.passer_img, (690, 385))
            self.fenetre.blit(retourne.img, (473, 276))
        pygame.display.flip()

