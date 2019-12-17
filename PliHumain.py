# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""
from Regle import regle
from CompareCarteJeu import compareCarteJeu
from AfficheJeu import affichageJeu
from AffichageTexte import affichageTexte
from AffichageOuiNon import affichageOuiNon
from OrdreJoueur import ordreJoueur

def pliHumain(jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, num_joueur,joueurs,gagnant,gagnant_prec):
    """Fonction qui permet à un humain de jouer. Prend en argument son jeu, les cartes actuelles du pli, le joueur qui a fait une belote et une rebelote, la carte meneuse, le numéro du pli et le numéro du joueur"""
    n_joueur=(num_joueur-gagnant_prec)%4
    jo=ordreJoueur(joueurs[gagnant_prec-1][0], joueurs)
    if gagnant ==4 :
        gagn = 4
    else :
        gagn= (gagnant-gagnant_prec)%4
    autorise = False
    while not autorise: # Tant que la carte que l'on veut jouer n'est pas autorisée par les règles
        choix = int(affichageJeu(cartes_pli,jeu,gagn,couleur_atout,jo[n_joueur][0],jo))
        if regle(jeu, cartes_pli, jeu[choix-1], couleur_atout, carte_meneuse):
            autorise = True
        else:
            affichageTexte("Vous n'êtes pas autorisé à jouer cette carte")
    if jeu[choix-1][1]==couleur_atout and jeu[choix-1][0] in ["Dame", "Roi"] and belote==4: # Si l'humain est dans une situation de belote, on lui demande s'il veut la déclarer
        belote = affichageOuiNon("Belote ?",["y","n"])
    elif jeu[choix-1][1]==couleur_atout and jeu[choix-1][0] in ["Dame", "Roi"] and belote==num_joueur: # Si l'humain est dans une situation de rebelote, on lui demande s'il veut la déclarer
        rebelote = affichageOuiNon("Rebelote ?",["y","n"])
    cartes_pli.append(jeu[choix-1]) # On ajoute à la liste des cartes du pli celles que le joueur vient de jouer
    if belote == "y": # Update des variables belote et rebelote
        belote = num_joueur
    elif belote == "n":
        belote = 4
    if rebelote == "y":
        rebelote = num_joueur
    elif rebelote == "n":
        rebelote = 4
    jeu.pop(choix-1) # On enlève la carte qui vient d'être jouée au jeu du joueur
    return jeu, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse
