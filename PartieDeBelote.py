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
from Regle import regle
#mettre une condition pour que 2 personnes ne puissent pas avoir le meme nom

def partieDeBelote():
    print('phase de distribution')
    paquet_de_carte = creationPaquetDeCartes()
    paquet_de_carte = melangeCarte(paquet_de_carte)
    equipe_1=[]
    equipe_2=[]
    joueur=input("joueur 1 de l\'equipe 1: ")
    equipe_1.append(str(joueur))
    joueur=input("joueur 2 de l\'equipe 1: ")
    equipe_1.append(str(joueur))
    joueur=input("joueur 1 de l\'equipe 2: ")
    equipe_2.append(str(joueur))
    joueur=input("joueur 2 de l\'equipe 2: ")
    equipe_2.append(str(joueur))
    joueur=[equipe_1[0],equipe_2[0],equipe_1[1],equipe_2[1]]
    tirage1=str(input("joueur equipe 1 qui tire au sort une carte: "))
    while (tirage1!=equipe_1[0] and tirage1!= equipe_1[1]):
        print(tirage1+',ce n\'est pas un joueur de votre equipe, choisissez dans '+equipe_1[0]+' et ' + equipe_1[1])
        tirage1=str(input("joueur equipe 1 qui tire au sort une carte: "))
    tirage2=str(input("joueur equipe 2 qui tire au sort une carte: "))
    while (tirage2!= equipe_2[0] and tirage2!= equipe_2[1]):
        print(tirage2+',ce n\'est pas un joueur de votre equipe, choisissez dans '+equipe_2[0]+' et ' + equipe_2[1])
        tirage2=str(input("joueur equipe 2 qui tire au sort une carte: "))
    pre_joueur, carte_equipe_1, carte_equipe_2 =premierJoueur(tirage1,tirage2,paquet_de_carte)
    print('\n')
    print(pre_joueur + ' est le joueur qui commence, le joueur de l\'equipe 1 a tiré ['+str(carte_equipe_1[0])+','+str(carte_equipe_1[1])+'] tandis que le joueur de l\'equipe 2 a tiré ['+str(carte_equipe_2[0])+','+str(carte_equipe_2[1])+']')
    joueur = ordreJoueur(pre_joueur, joueur)
    jeu1,jeu2,jeu3,jeu4,atout = distribution(paquet_de_carte)
    

    
    
    
    
    

