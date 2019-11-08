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
    print('phase de distribution')
    paquet_de_carte = creationPaquetDeCartes()
    paquet_de_carte = melangeCarte(paquet_de_carte)
    equipe_1=[]
    equipe_2=[]
    type_de_partie = str(input("voulez vous faire une partie aux points ou aux tours? (p/t)"))
    while type_de_partie != 't' and type_de_partie !='p' :
        print("Vous n\'avez pas donné de réponse correcte")
        type_de_partie = str(input("voulez vous faire une partie aux points ou aux tours? (p/t)"))
    if type_de_partie=="p":
        points_max = int(input("combien de points maximum?"))
    elif type_de_partie=="t" :
        tours_max = int(input("Nombre de tours? "))
    joueur=input("joueur 1 de l\'equipe 1: ")
    race = input("1. humain ou 2. IA : ")
    if race == 1:
        race = "Humain"
    else:
        race = "IA"
    equipe_1.append([str(joueur), race])
    joueur=input("joueur 2 de l\'equipe 1: ")
    joueur = str(joueur)
    while (joueur in equipe_1 or joueur =='') :
        print("ce nom est déjà pris")
        joueur=input("joueur 2 de l\'equipe 1: ")
        joueur = str(joueur)
    race = input("1. humain ou 2. IA : ")
    if race == 1:
        race = "Humain"
    else:
        race = "IA"
    equipe_1.append([str(joueur), race])
    joueur=input("joueur 1 de l\'equipe 2: ")
    joueur = str(joueur)
    while (joueur in equipe_1 or joueur =='') :
        print("ce nom est déjà pris")
        joueur=input("joueur 1 de l\'equipe 2: ")
        joueur = str(joueur)
    race = input("1. humain ou 2. IA : ")
    if race == 1:
        race = "Humain"
    else:
        race = "IA"
    equipe_2.append([str(joueur), race])
    joueur=input("joueur 2 de l\'equipe 2: ")
    joueur = str(joueur)
    while (joueur in equipe_1 or joueur in equipe_2 or joueur =='') :
        print("ce nom est déjà pris")
        joueur=input("joueur 2 de l\'equipe 2: ")
        joueur = str(joueur)
    race = input("1. humain ou 2. IA : ")
    if race == 1:
        race = "Humain"
    else:
        race = "IA"
    equipe_2.append([str(joueur), race])
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
    if type_de_partie=="p":
        while points_1<points_max and points_2<points_max:
            print("le joueur qui commence est :" + joueur[0][0])
            paquet_de_carte = melangeCarte(paquet_de_carte)
            jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte,joueur)
            print("le preneur est: " + joueur[preneur][0])
            plis_equipe1, plis_equipe2, gagnant, belote = jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout,joueur)
            if joueur[0][0] in equipe_1 : 
                p1,p2=calculPoint(plis_equipe1, plis_equipe2, gagnant, atout, belote)
            else :
                p1,p2=calculPoint(plis_equipe2, plis_equipe1, gagnant, atout, belote)
            if joueur[preneur] in equipe_1 : 
                points_1,points_2 = updateScore(points_1, points_2, p1, p2, 1)
            else : 
                points_1,points_2 = updateScore(points_1, points_2, p1, p2, 2)
            print("le score de l\' équipe 1 est: " , points_1)
            print("\n")
            print("le score de l\' équipe 2 est: ", points_2)
            joueur= ordreJoueur(joueur[0][0],joueur)
    if type_de_partie=="t":
        for k in range(tours_max):
            print("le joueur qui commence est :" + joueur[0][0])
            paquet_de_carte = melangeCarte(paquet_de_carte)
            jeu1,jeu2,jeu3,jeu4,atout,preneur = distribution(paquet_de_carte)
            print("le preneur est: " + joueur[preneur])
            plis_equipe1, plis_equipe2, gagnant, belote = jeuDeLaCarte(jeu1, jeu2, jeu3, jeu4, atout)
            if joueur[0][0] in equipe_1 : 
                p1,p2=calculPoint(plis_equipe1, plis_equipe2, gagnant, atout, belote)
            else :
                p1,p2=calculPoint(plis_equipe2, plis_equipe1, gagnant, atout, belote)
            if joueur[preneur] in equipe_1 : 
                points_1,points_2 = updateScore(points_1, points_2, p1, p2, 1)
            else : 
                points_1,points_2 = updateScore(points_1, points_2, p1, p2, 2)
            print("le score de l\' équipe 1 est: ", points_1)
            print("le score de l\' équipe 2 est: ", points_2)
            print("\n")
            joueur= ordreJoueur(joueur[0][0],joueur)
    
    
    
    
    

    
    
    
    
    

