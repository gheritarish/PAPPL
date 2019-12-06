# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:39:49 2019

@author: alepe
"""
#import Distribution
from CreationPaquetDeCartes import creationPaquetDeCartes
from MelangeCarte import melangeCarte
from PremierJoueur import premierJoueur
from OrdreJoueur import ordreJoueur
from Distribution import distribution
from JeuDeLaCarte import jeuDeLaCarte
from CalculPoint import calculPoint
from UpdateScore import updateScore
#mettre une condition pour que 2 personnes ne puissent pas avoir le meme nom

def partieDeBelote():
    """Fonction qui permet de gérer l'intégralité de la partie de belote en faisant appel aux autres fonctions"""
    print('phase de distribution')
    paquet_de_carte = creationPaquetDeCartes()
    paquet_de_carte = melangeCarte(paquet_de_carte)
    equipe_1=[]
    equipe_2=[]
    type_de_partie = str(input("voulez vous faire une partie aux points ou aux tours? (p/t)")) # On demande aux joueurs quelle type de partie ils souhaitent faire
    while type_de_partie != 't' and type_de_partie !='p' :
        print("Vous n\'avez pas donné de réponse correcte")
        type_de_partie = str(input("voulez vous faire une partie aux points ou aux tours? (p/t)"))
    if type_de_partie=="p":
        points_max = int(input("combien de points maximum?"))
    elif type_de_partie=="t" :
        tours_max = int(input("Nombre de tours? "))
    joueur=input("joueur 1 de l\'equipe 1: ")
    gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente : ")
    race = int(gender)
    while race != 1 and race != 2 and race!= 3:
        print("Ceci n'est pas 1 ou 2 ou 3")
        gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente: ")
        race = int(gender)
    if race == 1:
        race = "Humain"
    elif race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_1.append([str(joueur), race])
    joueur=input("joueur 2 de l\'equipe 1: ")
    joueur = str(joueur)
    while (joueur in equipe_1 or joueur =='') :
        print("ce nom est déjà pris")
        joueur=input("joueur 2 de l\'equipe 1: ")
        joueur = str(joueur)
    gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente : ")
    race = int(gender)
    while race != 1 and race != 2 and race !=3 :
        print("Ceci n'est pas 1 ou 2 ou 3")
        gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente : ")
        race = int(gender)
    if race == 1:
        race = "Humain"
    elif race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_1.append([str(joueur), race])
    joueur=input("joueur 1 de l\'equipe 2: ")
    joueur = str(joueur)
    while (joueur in equipe_1 or joueur =='') :
        print("ce nom est déjà pris")
        joueur=input("joueur 1 de l\'equipe 2: ")
        joueur = str(joueur)
    gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente : ")
    race = int(gender)
    while race != 1 and race != 2 and race!=3 :
        print("Ceci n'est pas 1 ou 2 ou 3")
        gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente : ")
        race = int(gender)
    if race == 1:
        race = "Humain"
    elif race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_2.append([str(joueur), race])
    joueur=input("joueur 2 de l\'equipe 2: ")
    joueur = str(joueur)
    while (joueur in equipe_1 or joueur in equipe_2 or joueur =='') :
        print("ce nom est déjà pris")
        joueur=input("joueur 2 de l\'equipe 2: ")
        joueur = str(joueur)
    gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente ")
    race = int(gender)
    while race != 1 and race != 2 and race!=3 :
        print("Ceci n'est pas 1 ou 2 ou 3")
        gender = input("1. humain ou 2. IAdebile ou 3. IAintelligente ")
        race = int(gender)
    if race == 1:
        race = "Humain"
    elif race==2:
        race="IAaleatoire"
    else:
        race = "IAminimax"
    equipe_2.append([str(joueur), race])
    diffi = input("rentrer le niveau de difficulter des IA (entier) : ")
    difficulte = int(diffi)
    joueur=[equipe_1[0],equipe_2[0],equipe_1[1],equipe_2[1]]
    tirage1=str(input("joueur equipe 1 qui tire au sort une carte: "))
    while (tirage1!=equipe_1[0][0] and tirage1!= equipe_1[1][0]):
        print(tirage1+',ce n\'est pas un joueur de votre equipe, choisissez dans '+equipe_1[0][0]+' et ' + equipe_1[1][0])
        tirage1=str(input("joueur equipe 1 qui tire au sort une carte: "))
    tirage2=str(input("joueur equipe 2 qui tire au sort une carte: "))
    while (tirage2!= equipe_2[0][0] and tirage2!= equipe_2[1][0]):
        print(tirage2+',ce n\'est pas un joueur de votre equipe, choisissez dans '+equipe_2[0][0]+' et ' + equipe_2[1][0])
        tirage2=str(input("joueur equipe 2 qui tire au sort une carte: "))
    pre_joueur, carte_equipe_1, carte_equipe_2 =premierJoueur(tirage1,tirage2,paquet_de_carte)
    print('\n')
    print(pre_joueur + ' est le joueur qui distribue, le joueur de l\'equipe 1 a tiré ['+str(carte_equipe_1[0])+','+str(carte_equipe_1[1])+'] tandis que le joueur de l\'equipe 2 a tiré ['+str(carte_equipe_2[0])+','+str(carte_equipe_2[1])+']')
    joueur = ordreJoueur(pre_joueur, joueur)
    points_1=0
    points_2=0
    score_reporte = 0
    if type_de_partie=="p": # Dans le cas d'une partie aux points
        while (points_1<points_max and points_2<points_max) or score_reporte != 0:
            print("le joueur qui commence est :" + joueur[0][0])
            paquet_de_carte = melangeCarte(paquet_de_carte)
            jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte,joueur)
            print("le preneur est: " + joueur[preneur][0])
            plis_equipe1, plis_equipe2, gagnant, belote = jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout,joueur,difficulte,preneur)
            if joueur[0][0] in equipe_1 : 
                p1, p2, equipe_belote = calculPoint(plis_equipe1, plis_equipe2, gagnant, atout, belote)
            else :
                p1, p2, equipe_belote = calculPoint(plis_equipe2, plis_equipe1, gagnant, atout, belote)
            if joueur[preneur] in equipe_1 : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 1, equipe_belote, score_reporte)
            else : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 2, equipe_belote, score_reporte)
            print("le score de l\' équipe 1 est: " , points_1)
            print("le score de l\' équipe 2 est: ", points_2)
            print("\n")
            joueur= ordreJoueur(joueur[0][0],joueur)
    if type_de_partie=="t": # Dans le cas d'une partie au nombre de donnes
        k = 0
        while k < tours_max or score_reporte != 0:
            print("le joueur qui commence est :" + joueur[0][0])
            paquet_de_carte = melangeCarte(paquet_de_carte)
            jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte, joueur)
            print("le preneur est: " + joueur[preneur][0])
            plis_equipe1, plis_equipe2, gagnant, belote = jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout, joueur,difficulte,preneur)
            if joueur[0][0] in equipe_1 : 
                p1, p2, equipe_belote = calculPoint(plis_equipe1, plis_equipe2, gagnant, atout, belote)
            else :
                p1, p2, equipe_belote = calculPoint(plis_equipe2, plis_equipe1, gagnant, atout, belote)
            if joueur[preneur] in equipe_1 : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 1, equipe_belote, score_reporte)
            else : 
                points_1,points_2, score_reporte = updateScore(points_1, points_2, p1, p2, 2, equipe_belote, score_reporte)
            print("le score de l\' équipe 1 est: ", points_1)
            print("le score de l\' équipe 2 est: ", points_2)
            print("\n")
            joueur= ordreJoueur(joueur[0][0],joueur)
            k += 1
    
    
    
    

    
    
    
    
    

