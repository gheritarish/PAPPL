# -*- coding=utf-8 -*-
"""
Created on Tue Oct 22 17:13:30 2019

@author: telmar
"""
from PliIA import pliIA
def jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout,joueur):
    """Le joueur 4 n'existe pas. Belote reste à joueur 4 si personne ne l'a"""
    cartes0 = [] # Les cartes que n'a pas le joueur 0
    cartes1 = [] # Les cartes que n'a pas le joueur 1
    cartes2 = [] # Les cartes que n'a pas le joueur 2
    cartes3 = [] # Les cartes que n'a pas le joueur 3
    paquet = creationPaquetDeCartes()
    for carte in paquet: # Pour initialiser les cartes que n'ont pas chacun des joueurs
        if carte not in jeu1:
            cartes0.append(carte)
        if carte not in jeu2:
            cartes1.append(carte)
        if carte not in jeu3:
            cartes2.append(carte)
        if carte not in jeu4:
            cartes3.append(carte)
    cartes_jouees = []
    belote = 4
    rebelote=4
    gagnant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    numero_pli=0
    for i in range(8):
        jeu1, jeu2, jeu3, jeu4,gagnant, plis,belote,rebelote = pliIA(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote,rebelote, atout,joueur,numero_pli)
        gagnant_prec = gagnant
        if gagnant in [0,2]:
            plis_equipe1.append(plis)
        else:
            plis_equipe2.append(plis)
        numero_pli=numero_pli+1
        for carte in plis:
            cartes_jouees.append(carte)
            if carte in cartes0:
                cartes0.pop(carte)
            if carte in cartes1:
                cartes1.pop(carte)
            if carte in cartes2:
                cartes2.pop(carte)
            if carte in cartes3:
                cartes3.pop(carte)
    return plis_equipe1, plis_equipe2, gagnant, rebelote
