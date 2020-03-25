# -*- coding=utf-8 -*-
"""
Created on Tue Mar 24 15:54:30 2020

@author: clegui
"""
from Pli import pli
from CreationPaquetDeCartes import creationPaquetDeCartes
from SuppressionCartes import suppressionCartes
from OrdreJoueur import ordreJoueur

def jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout,joueur,difficulte,preneur):
    """Fonction qui permet de gérer les plis. Les 4 jeux sont des listes de carte, atout est la couleur de l'atout et joueur le premier joueur"""
    belote = 4 # Le joueur 4 n'existe pas, belote et rebelote restent à 4 si personne ne les a
    rebelote=4
    gagnant_prec = 0
    plis_equipe1 = []
    plis_equipe2 = []
    cartes_restantes = creationPaquetDeCartes()
    numero_pli=0
    j=ordreJoueur(joueur[gagnant_prec-1][0], joueur)
    jeu1, jeu2, jeu3, jeu4, gagnant, plis, belote, rebelote = pli(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote, rebelote, atout, joueur, numero_pli,difficulte,preneur,plis_equipe1,plis_equipe2)
    gagnant_prec = gagnant
    if gagnant in [0,2]: # On ajoute le pli qui vient d'être fait à l'équipe qui l'a fait
        plis_equipe1.append(plis)
    else:
        plis_equipe2.append(plis)
    numero_pli=numero_pli+1
    cartes_restantes = suppressionCartes(cartes_restantes, plis)

    return plis_equipe1, plis_equipe2, gagnant, rebelote # On renvoie les plis des deux équipes, le gagnant du dernier pli et le joueur qui a fait la rebelote (il a nécessairement fait une belote aussi)


