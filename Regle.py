# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:44:07 2019

@author: alepe
"""

def regle(jeu,pli,carte,atout,meneur):
    if pli==0: #cas du premier joueur
        return True
    elif len(pli)==1: #cas du second joueur
        if carte[1]==pli[0,1]: # on regarde si la couleur est identique
            if pli[0,1]!=atout or pli[0,0]<carte[0]: #si ce n'est pas de l'atout ou que la valeur est plus grande il a le droit
                return True
            else: # la couleur demandé est de l'atout et la carte est plus petite, il faut vérifier dans son jeu qu'il n'a pas d'atout plus grand
                for i in range(len(jeu)):
                    if jeu[i,1]==atout and jeu[i,0]> pli[0,0]:
                        return False
                return True
        else: #la couleur posée est différente
            for i in range(len(jeu)):
                if jeu[i,1]==pli[0,1]: # on vérifie si il n'y a pas de la couleur demandé dans le jeu
                    return False
            if carte[1]==atout : #si il y n'a pas de la couleur demandé et qu'il a joué un atout c'est bon 
                return True
            else : #sinon il faut vérifié qu'il n'a pas d'atout dans son jeu
                for i in range(len(jeu)):
                    if jeu[i,1]==atout:
                        return False
                return True
            
    elif len(pli)==2:
        if carte[1]==pli[0,1]: # on regarde si la couleur est identique
            if pli[0,1]!=atout: #si ce n'est pas de l'atout il a le droit
                return True
            else:# la couleur demandé est de l'atout, il faut vérifier dans son jeu qu'il n'a pas d'atout plus grand
                if carte[0]>meneur[0]:
                    return True
                else : 
                    for i in range(len(jeu)):
                        if jeu[i,1]==atout and jeu[i,0]> meneur[0]:
                            return False
                        return True
        else: #la couleur posée est différente
            for i in range(len(jeu)):
                if jeu[i,1]==pli[0,1]: # on vérifie si il n'y a pas de la couleur demandé dans le jeu
                    return False
            if meneur==pli[0] and pli[0,1]!=atout: #on regarde si notre partenaire est maitre et si c'est pas l'atout qui est demandé
                return True

            if carte[1]==atout and meneur[1] != atout: #si il y n'a pas de la couleur demandé et qu'il a joué un atout c'est bon 
                return True
            elif carte[1]==atout and meneur[1]==atout:
                if carte[0]>meneur[0]:
                    return True
                else:
                    for i in range(jeu):
                        if jeu[i,1]== atout and jeu[i,0]>meneur[0]:
                            return False
                    return True
            else : #sinon il faut vérifié qu'il n'a pas d'atout dans son jeu
                for i in range(len(jeu)):
                    if jeu[i,1]==atout:
                        return False
                return True    
            
    elif len(pli)==3:
        if carte[1]==pli[0,1]: # on regarde si la couleur est identique
            if pli[0,1]!=atout: #si ce n'est pas de l'atout il a le droit
                return True
            else:# la couleur demandé est de l'atout, il faut vérifier dans son jeu qu'il n'a pas d'atout plus grand
                if carte[0]>meneur[0]:
                    return True
                else : 
                    for i in range(len(jeu)):
                        if jeu[i,1]==atout and jeu[i,0]> meneur[0]:
                            return False
                        return True
        else: #la couleur posée est différente
            for i in range(len(jeu)):
                if jeu[i,1]==pli[0,1]: # on vérifie si il n'y a pas de la couleur demandé dans le jeu
                    return False
            if meneur==pli[1] and pli[0,1]!=atout: #on regarde si notre partenaire est maitre et si c'est pas l'atout qui est demandé
                return True

            if carte[1]==atout and meneur[1] != atout: #si il y n'a pas de la couleur demandé et qu'il a joué un atout c'est bon 
                return True
            elif carte[1]==atout and meneur[1]==atout:
                if carte[0]>meneur[0]:
                    return True
                else:
                    for i in range(jeu):
                        if jeu[i,1]== atout and jeu[i,0]>meneur[0]:
                            return False
                    return True
            else : #sinon il faut vérifié qu'il n'a pas d'atout dans son jeu
                for i in range(len(jeu)):
                    if jeu[i,1]==atout:
                        return False
                return True           
    
                   
        
        
    