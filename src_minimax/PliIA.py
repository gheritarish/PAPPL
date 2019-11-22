# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""
from Regle import regle
from CompareCarteJeu import compareCarteJeu
import random as rd
from CartesJouables import cartesJouables

def pliIA(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote,rebelote, couleur_atout,joueur,num_pli):
    joues = 0
    cartes_pli = []
    carte_meneuse = 0
    gagnant = 4
    while joues < 4:
        autorise=False
        cartes_possibles = []
        if (gagnant_prec + joues) % 4 == 0:
            cartes_possibles = cartesJouables(jeu1, cartes_pli, couleur_atout, carte_meneuse)
            jouer = rd.randint(1, len(cartes_possibles))
            card = cartes_possibles[jouer-1]
            cartes_pli.append(jeu1[card])
            if jeu1[card][1] == couleur_atout and jeu1[card][0] in ["Dame", "Roi"] and belote == 4:
                belote = 0
            elif jeu1[card][1] == couleur_atout and jeu1[card][0] in ["Dame", "Roi"] and belote == 0:
                rebelote = 0
            jeu1.pop(card)
        elif (gagnant_prec + joues) % 4 == 1:
            cartes_possibles = cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse)
            jouer = rd.randint(1, len(cartes_possibles))
            card = cartes_possibles[jouer-1]
            cartes_pli.append(jeu2[card])
            if jeu2[card][1] == couleur_atout and jeu2[card][0] in ["Dame", "Roi"] and belote == 4:
                belote = 1
            elif jeu2[card][1] == couleur_atout and jeu2[card][0] in ["Dame", "Roi"] and belote == 0:
                rebelote = 1
            jeu2.pop(card)
        elif (gagnant_prec + joues) % 4 == 2:
            cartes_possibles = cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse)
            jouer = rd.randint(1, len(cartes_possibles))
            card = cartes_possibles[jouer-1]
            cartes_pli.append(jeu3[card])
            if jeu3[card][1] == couleur_atout and jeu3[card][0] in ["Dame", "Roi"] and belote == 4:
                belote = 2
            elif jeu3[card][1] == couleur_atout and jeu3[card][0] in ["Dame", "Roi"] and belote == 0:
                rebelote = 2
                jeu3.pop(card)
        elif (gagnant_prec + joues) % 4 == 3:
            cartes_possibles = cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse)
            jouer = rd.randint(1, len(cartes_possibles))
            card = cartes_possibles[jouer-1]
            cartes_pli.append(jeu4[card])
            if jeu4[card][1] == couleur_atout and jeu4[card][0] in ["Dame", "Roi"] and belote == 4:
                belote = 3
            elif jeu4[card][1] == couleur_atout and jeu4[card][0] in ["Dame", "Roi"] and belote == 0:
                rebelote = 3
            jeu4.pop(card)
        
        if carte_meneuse == 0:
            carte_meneuse = cartes_pli[-1]
            gagnant=(gagnant_prec + joues) % 4
        else:
            gain = compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)
            if gain == -1:
                carte_meneuse = cartes_pli[-1]
                gagnant = (gagnant_prec + joues) % 4
            elif gain == 1:
                carte_meneuse = carte_meneuse
        
        joues += 1

 
    return jeu1, jeu2, jeu3, jeu4, gagnant, cartes_pli, belote,rebelote
