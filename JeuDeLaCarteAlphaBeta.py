# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:22:11 2020

@author: Jérôme VILLEROT
"""
from CartesJouables import cartesJouables
from CompareCarteJeu import compareCarteJeu
from CalculPointMinimax import calculPointMinimax
from UpdateScoreMinimax import updateScoreMinimax
from InitialiseInfini import initialiseInfini
from ActualiseExtremum import actualiseExtremum
from MiseAJourAB import miseAJourAB
from SortDeLIntervalle import sortDeLIntervalle
from LaBorne import laBorne
"""
Cette fonction sera appelé à la fin pour finir les tours de jeux pour chaque appel récurssif de l'IA 
paramètre:
    @jeu1, jeu2, jeu3, jeu4 = jeux des 4 joueurs (dans l'ordre où ils vont jouer ce tour!) ce sont des listes de cartes
    @couleur_atout = couleur de l'atout de cette manche, c'est un string
    @ difficulte = entier qui définie la difficulté de l'IA
    @ belote, rebelote = entre 0 et 4 suivant qu'une belote ou une rebelote ait été dite ou non
    @ plis_equipe1 = liste des plis de l'equipe 1 depuis le debut de la manche(un plis etant une liste de 4 cartes) jeu1 et jeu3 sont les joueurs de cette equipe
    @plis_equipe2 = liste des plis de l'equipe 2 depuis le debut de la manche(un plis etant une liste de 4 cartes) jeu2 et jeu3 sont les joueurs de cette equipe
    @ num_pli = entier entre 0 et 8 correspondant au numero du pli de la manche qui a été terminé (à 8 la manche est finis)
    @ positionIA= entier entre 0 et 3 qui correspond à la postion de l'IA dans ce tour
    @poids= liste des poids pour l'IA
    @preneur= entier entre 0 et 3 qui correspond au joueur qui a pris l'atout à cette manche

"""

#jeu1, jeu2, jeu3 , jeu4 doivent être ordonné à l'appel de la fonction
def jeuDeLaCarteAlphaBeta(jeu1,jeu2,jeu3,jeu4,couleur_atout, difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids,preneur, alpha_precedent, beta_precedent):
    if len(jeu1)==0: #condition d'arret, on est au dernier pli et la derniere carte est jouée
        if positionIA in [0,2]: # ATTENTION : on ne connait pas encore gagnant_der           
            points1, points2 = calculPointMinimax(plis_equipe1, plis_equipe2, 1, couleur_atout, rebelote) # On calcule les points de l'équipe, les points de l'équipe 2 ne sont pas importants
            points_1,points_2 = updateScoreMinimax(0, 0, points1, points2, preneur)

                
            if rebelote in [0, 1, 2, 3]: # On définit un poids égal au score de l'équipe qu'elle fait en jouant ainsi - le nombre de points nécessaires pour remporter le contrat
                poids = points_1 - 91
            else:
                poids = points_1 - 81
            return poids
        else:
            points1, points2 = calculPointMinimax(plis_equipe1, plis_equipe2, 1, couleur_atout, rebelote) # Les points de l'équipe 1 ne sont pas intéressants
            points_1,points_2 = updateScoreMinimax(0, 0, points1, points2, preneur)
 
                
            if rebelote in [0, 1, 2, 3]:
                poids = points_2 - 91
            else:
                poids = points_2 - 81
            return poids
    elif ((num_pli==3) and (len(jeu1)==5)) or ((num_pli==3) and (len(jeu1)==4)) or ((num_pli==3) and (len(jeu1)==3)) :
        if positionIA in [0,2]: # ATTENTION : on ne connait pas encore gagnant_der           
            points1, points2 = calculPointMinimax(plis_equipe1, plis_equipe2, 1, couleur_atout, rebelote) # On calcule les points de l'équipe, les points de l'équipe 2 ne sont pas importants
            point_intermediare = 152 - points1 - points2
            points_1,points_2 = updateScoreMinimax(0, 0, points1 + point_intermediare//2, points2+ point_intermediare//2, preneur)
            
                
            if rebelote in [0, 2]: # On définit un poids égal au score de l'équipe qu'elle fait en jouant ainsi - le nombre de points nécessaires pour remporter le contrat
                poids = points_1 - 91
            else:
                poids = points_1 - 81
            return poids
        else:
            points1, points2 = calculPointMinimax(plis_equipe1, plis_equipe2, 1, couleur_atout, rebelote) # Les points de l'équipe 1 ne sont pas intéressants
            point_intermediare = 152 - points1 - points2
            points_1,points_2 = updateScoreMinimax(0, 0, points1+ point_intermediare//2, points2+ point_intermediare//2, preneur)
 
                
            if rebelote in [1, 3]:
                poids = points_2 - 91
            else:
                poids = points_2 - 81
            return poids        
    else : 
        cartes_pli=[]
        carte_meneuse0=0
        v0 = initialiseInfini(0,positionIA)#fonction qui renvoie -inf si le 1er joueur est avec l'IA, +inf sinon
        exploration_0_utile = True #au début, il est utile d'explorer --> on initialise exploration_utile
        nbCartesJouables_0 = len(cartesJouables(jeu1, cartes_pli, couleur_atout, carte_meneuse0)) #on calcule le nombre de cartes jouables possibles 
        i0 = 0 #on initialise i
        alpha0, beta0 = str('-inf'), str('inf')
        v0 = None
        while (exploration_0_utile and (i0 < nbCartesJouables_0)): #on parcours la liste des cartes jouables tant que l'exploration est utile et qu'il reste des cartes jouables à explorer
            carte1 = cartesJouables(jeu1, cartes_pli, couleur_atout, carte_meneuse0)[i0] #on prend la carte jouable suivante
            i0 = i0 + 1 #on incrémente i
            cartes_pli.append(carte1)
            carte_meneuse1 = cartes_pli[-1]
            gagnant1=1
            if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==4:
                belote1=0
            else :
                belote1=belote
            if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==0:
                rebelote1 = 0
            else:
                rebelote1 = rebelote
            v1 = initialiseInfini(1,positionIA)#fonction qui renvoie -inf si le 2eme joueur est avec l'IA, +inf sinon
            exploration_1_utile = True #au début, il est utile d'explorer --> on initialise exploration_utile
            nbCartesJouables_1 = len(cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse1)) #on calcule le nombre de cartes jouables possibles 
            i1 = 0 #on initialise i
            alpha1, beta1 = str('-inf'), str('inf')
            v1 = None
            while (exploration_1_utile and (i1 < nbCartesJouables_1)): #on parcours la liste des cartes jouables tant que l'exploration est utile et qu'il reste des cartes jouables à explorer
                carte2 = cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse1)[i1] #on prend la carte jouable suivante
                i1 = i1 + 1 #on incrémente i
                cartes_pli.append(carte2)
                if compareCarteJeu(carte_meneuse1, cartes_pli[-1], couleur_atout)==-1:
                    carte_meneuse2=cartes_pli[-1]
                    gagnant2=2
                else :
                    carte_meneuse2=carte_meneuse1
                    gagnant2=gagnant1
                if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote1==4:
                    belote2=1
                else :
                    belote2=belote1
                if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote1==1:
                    rebelote2 = 1
                else:
                    rebelote2 = rebelote1
                v2 = initialiseInfini(2,positionIA)#fonction qui renvoie -inf si le 3eme joueur est avec l'IA, +inf sinon
                exploration_2_utile = True #au début, il est utile d'explorer --> on initialise exploration_utile
                nbCartesJouables_2 = len(cartesJouables(jeu3, cartes_pli, couleur_atout, carte_meneuse2)) #on calcule le nombre de cartes jouables possibles 
                i2 = 0 #on initialise i
                alpha2, beta2 = str('-inf'), str('inf')
                v2 = None
                while (exploration_2_utile and (i2 < nbCartesJouables_2)): #on parcours la liste des cartes jouables tant que l'exploration est utile et qu'il reste des cartes jouables à explorer
                    carte3 = cartesJouables(jeu3, cartes_pli, couleur_atout, carte_meneuse2)[i2] #on prend la carte jouable suivante
                    i2 = i2 + 1 #on incrémente i
                    cartes_pli.append(carte3)
                    if compareCarteJeu(carte_meneuse2, cartes_pli[-1], couleur_atout)==-1:
                        carte_meneuse3=cartes_pli[-1]
                        gagnant3=3
                    else :
                        carte_meneuse3=carte_meneuse2
                        gagnant3=gagnant2
                    if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote2==4:
                        belote3=2
                    else :
                        belote3=belote2
                    if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote2==2:
                        rebelote3 = 2
                    else:
                        rebelote3 = rebelote2
                    v3 = initialiseInfini(3,positionIA)#fonction qui renvoie -inf si le 4eme joueur est avec l'IA, +inf sinon
                    exploration_3_utile = True #au début, il est utile d'explorer --> on initialise exploration_utile
                    nbCartesJouables_3 = len(cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3)) #on calcule le nombre de cartes jouables possibles 
                    i3 = 0 #on initialise i
                    alpha3, beta3 = str('-inf'), str('inf')
                    v3 = None
                    while (exploration_3_utile and (i3 < nbCartesJouables_3)): #on parcours la liste des cartes jouables tant que l'exploration est utile et qu'il reste des cartes jouables à explorer
                        carte4 = cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3)[i3] #on prend la carte jouable suivante
                        i3 = i3 + 1 #on incrémente i
                        cartes_pli.append(carte4)
                        if compareCarteJeu(carte_meneuse3, cartes_pli[-1], couleur_atout)==-1:
                            carte_meneuse4=cartes_pli[-1]
                            gagnant4=4
                        else :
                            carte_meneuse4=carte_meneuse3
                            gagnant4=gagnant3
                        j1=jeu1[:]
                        j1.remove(carte1)
                        j2=jeu2[:]
                        j2.remove(carte2)
                        j3=jeu3[:]
                        j3.remove(carte3)
                        j4=jeu4[:]
                        j4.remove(carte4)
                        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote3==4:
                            belote4=3
                        else :
                            belote4=belote3
                        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote3==3:
                            rebelote4 = 3
                        else:
                            rebelote4 = rebelote3
                        if gagnant4 ==1:
                            plis_equipe1.append(cartes_pli)                            
                            poids=jeuDeLaCarteAlphaBeta(j1,j2,j3,j4,couleur_atout,difficulte,belote4,rebelote4,plis_equipe1,plis_equipe2,num_pli+1,positionIA,poids,preneur)
                            plis_equipe1.remove(cartes_pli)
                            
                        if gagnant4 ==2:
                            plis_equipe2.append(cartes_pli)                            
                            poids=jeuDeLaCarteAlphaBeta(j2,j3,j4,j1,couleur_atout,difficulte,(belote4+1)%4,(rebelote4+1)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+1)%4,poids,(preneur+1)%2)
                            plis_equipe2.remove(cartes_pli)
                            
                        if gagnant4 ==3:
                            plis_equipe1.append(cartes_pli)                            
                            poids=jeuDeLaCarteAlphaBeta(j3,j4,j1,j2,couleur_atout, difficulte,(belote4+2)%4,(rebelote4+2)%4,plis_equipe1,plis_equipe2,num_pli+1,(positionIA+2)%4,poids,(preneur+2)%2)
                            plis_equipe1.remove(cartes_pli)
                            
                        if gagnant4 ==4:
                            plis_equipe2.append(cartes_pli)                            
                            poids=jeuDeLaCarteAlphaBeta(j4,j1,j2,j3,couleur_atout, difficulte,(belote4+3)%4,(rebelote4+3)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+3)%4,poids,(preneur+3)%2)
                            plis_equipe2.remove(cartes_pli)
                            
                        cartes_pli.pop(-1)
                        if (sortDeLIntervalle(poids, alpha2, beta2)):
                            exploration_3_utile = False
                        else:
                            v3 = actualiseExtremum(3,positionIA,v3,poids)#on actualise le score : on choisit le plus grand ou le plus petit, en fonction de si le joueur 4 est avec l'IA ou pas
                    cartes_pli.pop(-1)
                    if (exploration_3_utile):
                        alpha2, beta2 = miseAJourAB(v3, alpha2, beta2, 2, positionIA)
                        if (sortDeLIntervalle(laBorne(alpha2, beta2, 2, positionIA), alpha1, beta1)):
                            exploration_2_utile = False
                        else:
                            v2 = actualiseExtremum(2,positionIA,v2,v3)#on actualise le score : on choisit le plus grand ou le plus petit, en fonction de si le joueur 3 est avec l'IA ou pas
                cartes_pli.pop(-1)
                if (exploration_2_utile):
                    alpha1, beta1 = miseAJourAB(v2, alpha1, beta1, 1, positionIA)
                    if (sortDeLIntervalle(laBorne(alpha1, beta1, 1, positionIA), alpha0, beta0)):
                        exploration_1_utile = False
                    else:
                        v1 = actualiseExtremum(1,positionIA,v1,v2)#on actualise le score : on choisit le plus grand ou le plus petit, en fonction de si le joueur 2 est avec l'IA ou pas
            cartes_pli.pop(-1)
            if (exploration_1_utile):
                alpha0, beta0 = miseAJourAB(v1, alpha0, beta0, 0, positionIA)
                v0 = actualiseExtremum(0,positionIA,v0,v1)#on actualise le score : on choisit le plus grand ou le plus petit, en fonction de si le joueur 1 est avec l'IA ou pas
        return v0

