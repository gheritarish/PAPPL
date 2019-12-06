# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:31:29 2019

@author: alepe
"""
from CartesJouables import cartesJouables
from SuppressionCartes import suppressionCartes
from RedistributionIA import redistributionIA
import numpy as np
from JeuDeLaCarteMinimaxInitialise import jeuDeLaCarteMinimaxInitialise

'''
fonction à appelé pour avoir la liste des poids des cartes de l'IA
cartesIA = liste des cartes de notre IA
paquet = cartes qui n'ont pas été joué aux plis précédents
couleur_atout = couleur de l'atout
carte_meneuse = carte la plus forte du pli en cours (vaut 0 si aucune carte n'a été jouée)
meneur = position du meneur du pli en cours (valeur entre 1 et 4)
cartes_pli = liste des cartes du pli en cours
difficule = valeur strictement positif qui correspond à la force de l'IA
belote = y ou n selon qu'un joueur ait dis ou non belote
rebelote = y ou n suivant qu'un joueur ait dit ou non rebelote
plis_equipe1 = liste des plis de l'equipe 1 (c'est une liste de liste de cartes)
plis equipe2 = liste des plis de l'equipe 2
num_pli = numero du pli precedent
preneur = equipe qui a prise en debut de partie (vaut 1 ou 2)
'''
def 
:
    cartes_possibles=cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse) # on recupère les cartes jouables
    cartesAutreJoueur=suppressionCartes(suppressionCartes(paquet,cartes_pli), cartesIA) #cartes à redistribuer
    poids=np.zeros(len(cartes_possibles)) #matrice des poids de chaque cartes
    if len(cartes_pli)==0:
        positionIA=0
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitialise(cartesIA,jeu1,jeu2,jeu3,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur,preneur)
    if len(cartes_pli)==1:
        positionIA=1
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitialise(jeu1,cartesIA,jeu2,jeu3,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur,preneur) 
    if len(cartes_pli)==2:
        positionIA=2
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitialise(jeu1,jeu2,cartesIA,jeu3,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur,preneur) 
    if len(cartes_pli)==3:
        positionIA=3
        for i in range(difficulte):
            jeu1,jeu2,jeu3=redistributionIA(cartesAutreJoueur,len(cartes_pli)) #on a le jeu des autres
            for j in range(len(cartes_possibles)):
                poids[j]= poids[j] + jeuDeLaCarteMinimaxInitialise(jeu1,jeu2,jeu3,cartesIA,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids[j],j,carte_meneuse,meneur,preneur) 
    
    return poids
        

cartesIA = [['Roi','pique'],[7, 'trèfle'], [1, 'coeur']]
paquet=[['Roi','pique'],[7, 'trèfle'], [1, 'coeur'],['Valet', 'pique'],['Dame', 'pique'],['Roi', 'coeur'],['Valet', 'trèfle'],['Roi', 'trèfle'],[10, 'trèfle'],[10, 'carreau'],[7, 'carreau'],['Roi', 'carreau']]
couleur_atout='pique'
meneur=1
cartes_pli=[['Valet', 'pique'],['Dame', 'pique'],['Roi', 'coeur']]
carte_meneuse=['Valet', 'pique']
difficulte=10
belote='n'
rebelote='n'
plis_equipe1=[[[1, 'pique'],[7, 'pique'], [8, 'pique'], [9, 'pique']], [[10, 'pique'],[1, 'trèfle'],[8, 'trèfle'],['Dame', 'trèfle']],[[1, 'carreau'],[9, 'carreau'],['Dame', 'carreau'],['Valet', 'carreau']]]
plis_equipe2=[[[7, 'coeur'], [8, 'coeur'], [9, 'coeur'], [10, 'coeur']], [['Valet', 'coeur'], ['Dame', 'coeur'],[9, 'trèfle'],[8, 'carreau']]]
num_pli=5
preneur=1
        
    