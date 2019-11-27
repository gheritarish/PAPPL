# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:09:45 2019

@author: alepe
"""

from CartesJouables import cartesJouables
from CompareCarteJeu import compareCarteJeu
from SuppressionCartes import suppressionCartes
from JeuDeLaCarteMinimax import jeuDeLaCarteMinimax

def jeuDeLaCarteMinimaxInitialise(jeu1,jeu2,jeu3,jeu4, paquet,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poid,premiere_carte,carte_meneuse,meneur):
    if len(cartes_pli)==0:
        cartes_pli.append(jeu1[premiere_carte])
        carte_meneuse1=cartes_pli[-1]
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
                    if gagnant4==1:
                        poid=  jeuDeLaCarteMinimax(jeu1.remove(cartes_pli[1]),jeu2.remove(cartes_pli[1]),jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,positionIA,poid)
                        
                    elif gagnant4==2:
                        poid =  jeuDeLaCarteMinimax(jeu2.remove(cartes_pli[1]),jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]),jeu1.remove(cartes_pli[1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+1)%4,poid)
                        
                    elif gagnant4==3:
                        poid = jeuDeLaCarteMinimax(jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]),jeu1.remove(cartes_pli[1]),jeu2.remove(cartes_pli[1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,(positionIA+2)%4,poid)
                        
                    elif gagnant4==4:
                        poid =  jeuDeLaCarteMinimax(jeu4.remove(cartes_pli[-1]),jeu1.remove(cartes_pli[1]),jeu2.remove(cartes_pli[1]),jeu3.remove(cartes_pli[2]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+3)%4,poid)
                    cartes_pli.pop(-1)
                cartes_pli.pop(-1)
            cartes_pli.pop(-1)
        
    elif len(cartes_pli)==1:
        cartes_pli.append(jeu2[premiere_carte])
        if compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)==-1:
            carte_meneuse2=cartes_pli[-1]
            gagnant2=2
        else :
            carte_meneuse2=carte_meneuse
            gagnant2=meneur  
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
                if gagnant4==1:
                    poid=  jeuDeLaCarteMinimax(jeu1,jeu2.remove(cartes_pli[1]),jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,positionIA,poid)
                    
                elif gagnant4==2:
                    poid = jeuDeLaCarteMinimax(jeu2.remove(cartes_pli[1]),jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]),jeu1, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+1)%4,poid)
                    
                elif gagnant4==3:
                    poid = jeuDeLaCarteMinimax(jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]),jeu1,jeu2.remove(cartes_pli[1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,(positionIA+2)%4,poid)
                    
                elif gagnant4==4:
                    poid = jeuDeLaCarteMinimax(jeu4.remove(cartes_pli[-1]),jeu1,jeu2.remove(cartes_pli[1]),jeu3.remove(cartes_pli[2]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+3)%4,poid)
                cartes_pli.pop(-1)
            cartes_pli.pop(-1)
        
        
    elif len(cartes_pli)==2:
        cartes_pli.append(jeu3[premiere_carte])
        if compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)==-1:
            carte_meneuse3=cartes_pli[-1]
            gagnant3=3
        else :
            carte_meneuse3=carte_meneuse
            gagnant3=meneur
        for carte4 in cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3):
            cartes_pli.append(carte4)
            if compareCarteJeu(carte_meneuse3, cartes_pli[-1], couleur_atout)==-1:
                carte_meneuse4=cartes_pli[-1]
                gagnant4=4
            else :
                carte_meneuse4=carte_meneuse3
                gagnant4=gagnant3  
            if gagnant4==1:
                poid= jeuDeLaCarteMinimax(jeu1,jeu2,jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,positionIA,poid)
                
            elif gagnant4==2:
                poid = jeuDeLaCarteMinimax(jeu2,jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]),jeu1, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+1)%4,poid)
                
            elif gagnant4==3:
                poid = jeuDeLaCarteMinimax(jeu3.remove(cartes_pli[2]),jeu4.remove(cartes_pli[-1]),jeu1,jeu2, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,(positionIA+2)%4,poid)
                
            elif gagnant4==4:
                poid = jeuDeLaCarteMinimax(jeu4.remove(cartes_pli[-1]),jeu1,jeu2,jeu3.remove(cartes_pli[2]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+3)%4,poid)
            cartes_pli.pop(-1)       

        
    elif len(cartes_pli)==3:
        cartes_pli.append(jeu4[premiere_carte])
        if compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)==-1:
            carte_meneuse4=cartes_pli[-1]
            gagnant4=4
        else :
            carte_meneuse4=carte_meneuse
            gagnant4=meneur
        if gagnant4==1:
            poid= jeuDeLaCarteMinimax(jeu1,jeu2,jeu3,jeu4.remove(cartes_pli[-1]), paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,positionIA,poid)
            
        elif gagnant4==2:
            poid = jeuDeLaCarteMinimax(jeu2,jeu3,jeu4.remove(cartes_pli[-1]),jeu1, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+1)%4,poid)
            
        elif gagnant4==3:
            poid = jeuDeLaCarteMinimax(jeu3,jeu4.remove(cartes_pli[-1]),jeu1,jeu2, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe1.append(cartes_pli),plis_equipe2,num_pli+1,(positionIA+2)%4,poid)
            
        elif gagnant4==4:
            poid = jeuDeLaCarteMinimax(jeu4.remove(cartes_pli[-1]),jeu1,jeu2,jeu3, paquet,couleur_atout, difficulte,belote,rebelote,plis_equipe2.append(cartes_pli),plis_equipe1,num_pli+1,(positionIA+3)%4,poid)
    return poid