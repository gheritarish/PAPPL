# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""


from CompareCarteJeu import compareCarteJeu
from PliIA import pliIA
from PliHumain import pliHumain
from OrdreJoueur import ordreJoueur
from PliIAminimax import pliIAminimax
from AffichageTexte import affichageTexte

def pli(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote, rebelote, couleur_atout, joueur, num_pli,difficulte,preneur,plis_equipe1,plis_equipe2):
    """Fonction qui permet de gérer un pli. Prend en argument les jeux de chaque joueur, le joueur qui commence, le joueur qui a fait une belote, une rebelote, la couleur de l'atout, la liste des joueurs et le numéro du pli dans la donne"""
    cartes_pli = []
    carte_meneuse = 0
    gagnant = 4 # Désigne le gagnant du pli actuel, initialisé à 4 au début
    joues = 0 # Nombre de joueurs ayant déjà joué au cours du pli
    while joues < 4:

        if joueur[(gagnant_prec + joues) % 4][1] == "Humain": # Si le joueur est un humain
            affichageTexte("c'est au tour de " +joueur[(gagnant_prec + joues) % 4][0] )
            if (gagnant_prec + joues) % 4 == 0:
                jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 0,joueur,gagnant,gagnant_prec)
            elif (gagnant_prec + joues) % 4 == 1:
                jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 1,joueur,gagnant,gagnant_prec)
            elif (gagnant_prec + joues) % 4 == 2:
                jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli,2,joueur,gagnant,gagnant_prec)
            elif (gagnant_prec + joues) % 4 == 3:
                jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliHumain(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 3,joueur,gagnant,gagnant_prec)
        elif joueur[(gagnant_prec + joues) % 4][1] == "IAaleatoire": # Si le joueur est une IA aleatoire
            if (gagnant_prec + joues) % 4 == 0:
                jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 0)
            elif (gagnant_prec + joues) % 4 == 1:
                jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 1)
            elif (gagnant_prec + joues) % 4 == 2:
                jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 2)
            elif (gagnant_prec + joues) % 4 == 3:
                jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIA(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, num_pli, 3)
        else :#le joueur est une IA minimax
            if (gagnant_prec + joues) % 4 == 0:
                 if len(cartes_pli)==0 :
                     jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  0,difficulte,(gagnant-gagnant_prec)%4,preneur,plis_equipe1,plis_equipe2)
                 elif len(cartes_pli)==1:
                     jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  0,difficulte,(gagnant-gagnant_prec)%4,(preneur+1)%4,plis_equipe2,plis_equipe1)
                 elif len(cartes_pli)==2:
                     jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, 0,difficulte,(gagnant-gagnant_prec)%4,(preneur+2)%4,plis_equipe1,plis_equipe2)
                 elif len(cartes_pli)==3 :
                     jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu1, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, 0,difficulte,(gagnant-gagnant_prec)%4,(preneur+3)%4,plis_equipe2,plis_equipe1)
            elif (gagnant_prec + joues) % 4 == 1:
                if len(cartes_pli)==0 :
                    jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  1,difficulte,(gagnant-gagnant_prec)%4,(preneur-1)%4,plis_equipe2,plis_equipe1)
                elif len(cartes_pli)==1:
                    jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  1,difficulte,(gagnant-gagnant_prec)%4,preneur,plis_equipe1,plis_equipe2)
                elif len(cartes_pli)==2:
                    jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  1,difficulte,(gagnant-gagnant_prec)%4,(preneur+1)%4,plis_equipe2,plis_equipe1)
                elif len(cartes_pli)==3:
                    jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu2, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  1,difficulte,(gagnant-gagnant_prec)%4,(preneur+2)%4,plis_equipe1,plis_equipe2)
            elif (gagnant_prec + joues) % 4 == 2:
                if len(cartes_pli)==0 :
                    jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  2,difficulte,(gagnant-gagnant_prec)%4,(preneur-2)%4,plis_equipe1,plis_equipe2)
                elif len(cartes_pli)==1:
                    jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  2,difficulte,(gagnant-gagnant_prec)%4,(preneur-1)%4,plis_equipe2,plis_equipe1)
                elif len(cartes_pli)==2:
                    jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  2,difficulte,(gagnant-gagnant_prec)%4,preneur,plis_equipe1,plis_equipe2)
                elif len(cartes_pli)==3:
                    jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu3, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse, 2,difficulte,(gagnant-gagnant_prec)%4,(preneur+1)%4,plis_equipe2,plis_equipe1)
            elif (gagnant_prec + joues) % 4 == 3:
                if len(cartes_pli)==0 :
                    jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  3,difficulte,(gagnant-gagnant_prec)%4,(preneur-3)%4,plis_equipe2,plis_equipe1)           
                elif len(cartes_pli)==1:
                    jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  3,difficulte,(gagnant-gagnant_prec)%4,(preneur-2)%4,plis_equipe1,plis_equipe2)           
                elif len(cartes_pli)==2:
                    jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  3,difficulte,(gagnant-gagnant_prec)%4,(preneur-1)%4,plis_equipe2,plis_equipe1)           
                elif len(cartes_pli)==3:
                    jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse = pliIAminimax(jeu4, cartes_pli, belote, rebelote, couleur_atout, carte_meneuse,  3,difficulte,(gagnant-gagnant_prec)%4,preneur,plis_equipe1,plis_equipe2)
        
        if carte_meneuse == 0: # S'il n'y a pas encore de carte meneuse, c'est la seule carte qui a été jouée
            carte_meneuse = cartes_pli[-1]
            gagnant=(gagnant_prec + joues) % 4
        else: # S'il y a déjà une carte meneuse, on compare la carte qui vient d'être jouée avec l'ancienne carte meneuse
            gain = compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)
            if gain == -1:
                carte_meneuse = cartes_pli[-1]
                gagnant = (gagnant_prec + joues) % 4
        
        joues += 1

 
    return jeu1, jeu2, jeu3, jeu4, gagnant, cartes_pli, belote, rebelote
