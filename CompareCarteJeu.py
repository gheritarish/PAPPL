# -*- coding: utf-8 -*-
"""
Created on Wes Oct 23 14:30:35 2019

@author: telmar
"""

def compareCarteJeu(carte_meneuse, carte_jouee, atout):
    """Permet de comparer la carte qui vient d'être jouée et la carte meneuse pendant le jeu. Prend en argument deux cartes et la couleur de l'atout. Renvoie 1 si la carte meneuse gagne, -1 si la carte jouée gagne"""
    valeur_1 = carte_meneuse[0] # On retient les valeurs de chacune des cartes
    valeur_2 = carte_jouee[0]
    if carte_jouee[1] == carte_meneuse[1] and carte_meneuse[1] != atout: # Dans le cas où les deux cartes sont de la même couleur et qu'li n'y a pas d'atout
        if valeur_1==valeur_2:
        	return 0
        elif valeur_1==1:
        	return 1
        elif valeur_2==1:
        	return -1
        elif valeur_1 == 10:
            return 1
        elif valeur_2 == 10:
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
    else: # Si les couleurs sont différentes ou que l'une des deux cartes est à l'atout
        if carte_jouee[1] == atout: # Si la carte jouée est de l'atout
            if carte_meneuse[1] != atout: # Si la carte meneuse n'en est pas, elle perd
                return -1
            else: # Si la carte meneuse est de l'atout, on compare les valeurs
                if valeur_1 == "Valet":
                    return 1
                elif valeur_2 == "Valet":
                    return -1
                elif valeur_1 == 9:
                    return 1
                elif valeur_2 == 9:
                    return -1
                elif valeur_1 == 1:
                    return 1
                elif valeur_2 == 1:
                    return -1
                elif valeur_1 == 10:
                    return 1
                elif valeur_2 == 10:
                    return -1
                elif (type(valeur_1) == int and type(valeur_2) == int):
                    if valeur_1 > valeur_2:
                        return 1
                    else:
                        return -1
                elif (type(valeur_1) == str and type(valeur_2) == int):
                    return 1
                elif (type(valeur_1) == int and type(valeur_2) == str):
                    return -1
                elif (type(valeur_1) == str and type(valeur_2) == str):
                    if (valeur_1 == 'Roi'):
                        return 1
                    elif valeur_1 == 'Dame':
                        return -1
        else : # Si la carte meneuse est de l'atout et que la carte jouée n'en est pas, la carte meneuse est forcément maître

            return 1
