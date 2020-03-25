# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:54:37 2020

@author: clegui
"""
from CreationPaquetDeCartes import creationPaquetDeCartes
from MelangeCarte import melangeCarte
from PremierJoueur import premierJoueur
from OrdreJoueur import ordreJoueur
from Distribution import distribution
from JeuDeLaCarteGen import jeuDeLaCarte
from CalculPoint import calculPoint
from UpdateScore import updateScore
from AffichageTexteInput import affichageTexteInput
from AffichageOuiNon import affichageOuiNon
from Enregistrement import enregistre

"""
Cette fonction permet de générer des résultats de plis de belote en faisant appel aux autres fonctions
"""

def GenDeBelote():
    
    paquet_de_carte = creationPaquetDeCartes()
    paquet_de_carte = melangeCarte(paquet_de_carte)
    equipe_1=[]
    equipe_2=[]
    type_de_partie = "tours" # On demande aux joueurs quelle type de partie ils souhaitent faire
    if type_de_partie=="points":
        points_max = int(affichageOuiNon("combien de points maximum?",["100","200","300","400","500","1000"]))
    elif type_de_partie=="tours" :
        tours_max = int(affichageTexteInput("Combien de simulations ?"))
    joueur="1"
    gender = "3"# 2. IAdebile ou 3. IAintelligente : ",["2","3"]
    race = int(gender)
    if race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_1.append([str(joueur), race])
    joueur= "2" #"joueur 2 de l'equipe 1: "
    #joueur = str(joueur)
    while (joueur in equipe_1 or joueur =='') :
        joueur=affichageTexteInput("Ce nom est déjà pris, joueur 2 de l\'equipe 1: ")
        joueur = str(joueur)
    gender = "3" #2. IAdebile ou 3. IAintelligente : ",["2","3"]
    race = int(gender)
    if race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_1.append([str(joueur), race])
    joueur="3" #"joueur 1 de l'equipe 2: "
    while (joueur in equipe_1 or joueur =='') :
        joueur=affichageTexteInput("Ce nom est déjà pris, joueur 1 de l\'equipe 2: ")
        joueur = str(joueur)
    gender = "3" #2. IAdebile ou 3. IAintelligente : ",["2","3"]
    race = int(gender)
    if race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_2.append([str(joueur), race])
    joueur= "4" #joueur 2 de l'equipe 2:
    #joueur = str(joueur)
    while (joueur in equipe_1 or joueur in equipe_2 or joueur =='') :
        joueur= affichageTexteInput("Ce nom est déjà pris, joueur 2 de l\'equipe 2: ")
        joueur = str(joueur)
    gender = "3" #2. IAdebile ou 3. IAintelligente : ",["2","3"]
    race = int(gender)
    if race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_2.append([str(joueur), race])
    diffi = "100"#niveau de difficulté des IA (entier; 1: faible; 100 : fort) : ",["1", "5","10","25","50","100"]) --- 100 correspondant au minimax AlphaBeta
    difficulte = int(diffi)
    joueur=[equipe_1[0],equipe_2[0],equipe_1[1],equipe_2[1]]
    
    tirage1= "1"#joueur equipe 1 qui tire au sort une carte:
    while (tirage1!=equipe_1[0][0] and tirage1!= equipe_1[1][0]):
        tirage1=str(affichageTexteInput(tirage1+',ce n\'est pas un joueur de votre equipe, choisissez dans '+equipe_1[0][0]+' et ' + equipe_1[1][0] +", joueur equipe 1 qui tire au sort une carte: "))
    
    tirage2= "3"#"joueur equipe 2 qui tire au sort une carte: "
    while (tirage2!= equipe_2[0][0] and tirage2!= equipe_2[1][0]):
        tirage2=str(affichageTexteInput(tirage2+',ce n\'est pas un joueur de votre equipe, choisissez dans '+equipe_2[0][0]+' et ' + equipe_2[1][0]+", joueur equipe 2 qui tire au sort une carte: "))
    pre_joueur, carte_equipe_1, carte_equipe_2 =premierJoueur(tirage1,tirage2,paquet_de_carte)
    print('\n')
    joueur = ordreJoueur(pre_joueur, joueur)
    points_1=0
    points_2=0
    score_reporte = 0
    if type_de_partie=="points": # Dans le cas d'une partie aux points
        while (points_1<points_max and points_2<points_max) or score_reporte != 0:
            paquet_de_carte = melangeCarte(paquet_de_carte)
            jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte,joueur)
            while jeu1 == "On redistribue":
                jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte,joueur)
            plis_equipe1, plis_equipe2, gagnant, belote = jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout,joueur,difficulte,preneur)
            if joueur[0] in equipe_1 : 
                p1, p2, equipe_belote = calculPoint(plis_equipe1, plis_equipe2, gagnant, atout, belote)
            else :
                p1, p2, equipe_belote = calculPoint(plis_equipe2, plis_equipe1, gagnant, atout, belote)
            if joueur[preneur] in equipe_1 : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 1, equipe_belote, score_reporte)
            else : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 2, equipe_belote, score_reporte)
            joueur= ordreJoueur(joueur[0][0],joueur)
    if type_de_partie=="tours": # Dans le cas d'une partie au nombre de donnes
        k = 0
        while k < tours_max or score_reporte != 0:
            points_1=0
            points_2=0
            paquet_de_carte = melangeCarte(paquet_de_carte)
            jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte, joueur)
            nv_jeu = jeu1 + jeu2 + jeu3 + jeu4 #on obtient la répartition des cartes entre les 4 joueurs, on obtient ainsi les 4
            while jeu1 == "On redistribue":
                jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte,joueur)
            plis_equipe1, plis_equipe2, gagnant, belote = jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout, joueur,difficulte,preneur)
            #les cartes de chaque tour et l'issue du tour
            if joueur[0] in equipe_1 : 
                p1, p2, equipe_belote = calculPoint(plis_equipe1, plis_equipe2, gagnant, atout, belote)
            else :
                p1, p2, equipe_belote = calculPoint(plis_equipe2, plis_equipe1, gagnant, atout, belote)
            if joueur[preneur] in equipe_1 : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 1, equipe_belote, score_reporte)
            else : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 2, equipe_belote, score_reporte)
            joueur= ordreJoueur(joueur[0][0],joueur)
            k += 1
            if plis_equipe1 == []:
                enregistre(nv_jeu, "vide", plis_equipe2[0],gagnant, preneur, points_1, points_2,atout) #on indique vide lorsque l'équipe 1 n'a fait aucun pli et on aura v  dans la première colonne de l'équipe 1 puis i,... dans le fichier csv
            elif plis_equipe2 == []:
                enregistre(nv_jeu, plis_equipe1[0],"vide",gagnant, preneur, points_1, points_2,atout) #on indique vide lorsque l'équipe 2 n'a fait aucun pli et on aura v  dans la première colonne de l'équipe 2 puis i,... dans le fichier csv
            else:
                enregistre(nv_jeu, plis_equipe1[0], plis_equipe2[0],gagnant, preneur, points_1, points_2, atout)