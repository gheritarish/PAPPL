# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:57:10 2019

@author: telmar
"""
from EnchereT1IA import encherePremierTourIA
from EnchereT2IA import enchereDeuxiemeTourIA


def enchere(jeu1, jeu2, jeu3, jeu4, carte,joueur):
    """Fonction qui permet de gérer les enchères. Prend en argument les jeux de chacun des joueurs, la carte retournée et le premier joueur qui annonce. Renvoie une liste avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout, ou avec un unique élément "On redistribue"."""
    prise = encherePremierTourIA(jeu1, jeu2, jeu3, jeu4, carte,joueur)
    if prise[0] != "Personne n'a pris":
        return [prise[0], prise[1]]
    else:
        prise = enchereDeuxiemeTourIA(jeu1, jeu2, jeu3, jeu4, carte,joueur)
        if prise[0] != "Personne n'a pris":
            return [prise[0], prise[1]]
        else:
            return ["On redistribue"]
