# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:16:45 2019

@author: alepe
"""

def compareCarte(carte_1, carte_2): #en valeur, si carte_1>carte_2 renvoit 1, si carte_1<carte_2 renvoit -1, si carte_1=carte_2 renvoit 0
    """Fonction qui permet de comparer deux cartes en valeur pour savoir quelle équipe va commencer au tout début de la partie. Prend en argument deux cartes"""
    valeur_1 = carte_1[0]
    valeur_2 = carte_2[0]
    if valeur_1==valeur_2 :
        return 0
    elif valeur_1==1:
        return 1
    elif valeur_2==1:
        return -1
    elif (type(valeur_1)==int and type(valeur_2)==int):
        if valeur_1 > valeur_2 :
            return 1
        elif valeur_2> valeur_1 :
            return -1
    elif (type(valeur_1)==str and type(valeur_2)==int):
        return 1
    elif (type(valeur_2)==str and type(valeur_1)==int):
        return -1
    elif (type(valeur_2)==str and type(valeur_1)==str):
        if (valeur_1=='Valet'):
            return -1
        elif (valeur_1=='Roi'):
            return 1
        elif (valeur_2=='Valet'):
            return 1
        elif (valeur_2=='Roi'):
            return -1
    else :
        print('erreur dans CompareCarte')
        
        
        
