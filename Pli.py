# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""

def pli(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote, couleur_atout):
    joues = 0
    cartes_pli = []
    carte_meneuse = 0
    while joues < 4:
        for elt in cartes_pli:
        print("Cartes jouées :", elt[0], elt[1], "\n")
        print("Mon jeu :")
        if (gagnant_prec + joues) % 4 == 0:
			for i in range(len(jeu1)):
				print(i + 1, ":", elt[0], elt[1], "\n")
            choix = input("Quelle carte jouer ?")
            choix = int(choix)
            belote = input("Belote ? (y/n)")
            cartes_pli.append(jeu1[choix - 1])
            if belote == "y":
            	belote = (gagnant_prec + joues) % 4
            jeu1.pop(choix-1)
        elif (gagnant_prec + joues) % 4 == 1:
            for i in range(len(jeu2)):
                print(i + 1, ":", elt[0], elt[1], "\n")
            choix = input("Quelle carte jouer ?")
            choix = int(choix)
            belote = input("Belote ? (y/n)")
            cartes_pli.append(jeu2[choix - 1])
            if belote == "y":
            	belote = (gagnant_prec + joues) % 4
            jeu2.pop(choix-1)
        elif (gagant_prec + joues) % 4 == 2:
            for elt in jeu3:
                print(i + 1, ":", elt[0], elt[1], "\n")
            choix = input("Quelle carte jouer ?")
            choix = int(choix)
            belote = input("Belote ? (y/n)")
            cartes_pli.append(jeu3[choix - 1])
            if belote == "y":
            	belote = (gagnant_prec + joues) % 4
            jeu3.pop(choix-1)
       elif (gagnant_prec + joues) % 4 == 3:
            for elt in jeu4:
                print(i + 1, ":", elt[0], elt[1], "\n")
            choix = input("Quelle carte jouer ?")
            choix = int(choix)
            belote = input("Belote ? (y/n)")
            cartes_pli.append(jeu4[choix - 1])
            if belote == "y":
            	belote = (gagnant_prec + joues) % 4
            jeu4.pop(choix-1)
        joues += 1
        if carte_meneuse == 0:
            carte_meneuse = pli[-1]
        else:
            gain = compareCarteJeu(carte_meneuse, pli[-1], couleur_atout)
            if gain == 1:
            	carte_meneuse = pli[-1]
		
