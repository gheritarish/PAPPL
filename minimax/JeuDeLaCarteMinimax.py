# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:12:25 2019

@author: alepe
"""
from CartesJouables import cartesJouables
from CompareCarteJeu import compareCarteJeu
from SuppressionCartes import suppressionCartes

#jeu1, jeu2, jeu3 , jeu4 doivent être ordonné à l'appel de la fonction
def jeuDeLaCarteMinimax(jeu1,jeu2,jeu3,jeu4, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poids):
    if num_pli==8: #condition d'arret, on est au dernier pli et la derniere carte est jouée
        if positionIA in [0,2]: # ATTENTION : on ne connait pas encore gagnant_der
            points, inutile = calculPoints(plis_equipe1, plis_equipe2, gagnant_der, couleur_atout, rebelote) # On calcule les points de l'équipe, les points de l'équipe 2 ne sont pas importants
            if rebelote in [0, 2]: # On définit un poids égal au score de l'équipe qu'elle fait en jouant ainsi - le nombre de points nécessaires pour remporter le contrat
                poids = points - 91
            else:
                poids = points - 81
            return poids
        else:
            inutile, points = calculPoints(plis_equipe1, plis_equipe2, gagnant_der, couleur_atout, rebelote) # Les points de l'équipe 1 ne sont pas intéressants
            if rebelote in [1, 3]:
                poids = points - 91
            else:
                poids = points - 81
            return poids
        #il reste à calculer les scores et à update les poids ave le score
    else : 
        cartes_pli=[]
        carte_meneuse0=0
        for carte1 in cartesJouables(jeu1, cartes_pli, couleur_atout, carte_meneuse0):
            cartes_pli.append(carte1)
            carte_meneuse1 = cartes_pli[-1]
            gagnant1=1
            for carte2 in cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse1): 
                cartes_pli.append(carte2)
                if compareCarteJeu(carte_meneuse1, cartes_pli[-1], couleur_atout)==-1:
                    carte_meneuse2=cartes_pli[-1]
                    gagnant2=2
                else :
                    carte_meneuse2=carte_meneuse1
                    gagnant2=gagnant1
                for carte3 in cartesJouables(jeu3, cartes_pli, couleur_atout, carte_meneuse2): 
                    cartes_pli.append(carte3)
                    if compareCarteJeu(carte_meneuse2, cartes_pli[-1], couleur_atout)==-1:
                        carte_meneuse3=cartes_pli[-1]
                        gagnant3=3
                    else :
                        carte_meneuse3=carte_meneuse2
                        gagnant3=gagnant2
                    for carte4 in cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3): 
                        cartes_pli.append(carte4)
                        if compareCarteJeu(carte_meneuse3, cartes_pli[-1], couleur_atout)==-1:
                            carte_meneuse4=cartes_pli[-1]
                            gagnant4=4
                        else :
                            carte_meneuse4=carte_meneuse3
                            gagnant4=gagnant3
                        if gagnant4 ==1:
                            poids=jeuDeLaCarteMinimax(jeu1.remove(carte1),jeu2.remove(carte2),jeu3.remove(carte3),jeu4.remove(carte4), suppressionCartes(paquet,cartes_pli),couleur_atout,difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,positionIA,poids)
                        if gagnant4 ==2:
                            poids=jeuDeLaCarteMinimax(jeu2.remove(carte2),jeu3.remove(carte3),jeu4.remove(carte4),jeu1.remove(carte1), suppressionCartes(paquet,cartes_pli),couleur_atout,difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+1)%4,poids)
                        if gagnant4 ==3:
                            poids=jeuDeLaCarteMinimax(jeu3.remove(carte3),jeu4.remove(carte4),jeu1.remove(carte1),jeu2.remove(carte2), suppressionCartes(paquet,cartes_pli),couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,(positionIA+2)%4,poids)
                        if gagnant4 ==4:
                            poids=jeuDeLaCarteMinimax(jeu4.remove(carte4),jeu1.remove(carte1),jeu2.remove(carte2),jeu3.remove(carte3), suppressionCartes(paquet,cartes_pli),couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+3)%4,poids)
                        cartes_pli.pop(-1)
                    cartes_pli.pop(-1)
                cartes_pli.pop(-1)
            cartes_pli.pop(-1)
        return poids

            
