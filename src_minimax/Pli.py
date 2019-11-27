# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""
from Regle import regle
from CompareCarteJeu import compareCarteJeu
from PliIA import pliIA
from PliHumain import pliHumain
import random as rd

def pli(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote, rebelote, couleur_atout, joueur, num_pli):
    """Fonction qui permet de gérer un pli"""
    cartes_pli = []
    carte_meneuse = 0
    gagnant = 4
    joues = 0
    while joues < 4:
        if joueur[(gagnant_prec + joues) % 4][1] != "IA": # Si le joueur est un humain
            if (gagnant_prec + joues) % 4 == 0:
                jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 0)
            elif (gagnant_prec + joues) % 4 == 1:
                jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 1)
            elif (gagnant_prec + joues) % 4 == 2:
                jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 2)
            elif (gagnant_prec + joues) % 4 == 3:
                jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 3)
        else: # Si le joueur est une IA
            if (gagnant_prec + joues) % 4 == 0:
                jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 0)
            elif (gagnant_prec + joues) % 4 == 1:
                jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 1)
            elif (gagnant_prec + joues) % 4 == 2:
                jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 2)
            elif (gagnant_prec + joues) % 4 == 3:
                jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 3)

        if carte_meneuse == 0: # S'il n'y a pas encore de carte meneuse, c'est la seule carte qui a été jouée
            carte_meneuse = cartes_pli[-1]
            gagnant=(gagnant_prec + joues) % 4
        else: # S'il y a déjà une carte meneuse, on compare la carte qui vient d'être jouée avec l'ancienne carte meneuse
            gain = compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)
            if gain == -1:
                carte_meneuse = cartes_pli[-1]
                gagnant = (gagnant_prec + joues) % 4
            elif gain == 1:
                carte_meneuse = carte_meneuse
        
        joues += 1

 
    return jeu1, jeu2, jeu3, jeu4, gagnant, cartes_pli, belote, rebelote
