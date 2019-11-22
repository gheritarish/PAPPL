# -*- coding: utf-8 -*-
"""
Created on Wes Oct 23 14:30:35 2019

@author: telmar
"""

def compareCarteJeu(carte_meneuse, carte_jouee, atout):
    valeur_1 = carte_meneuse[0]
    valeur_2 = carte_jouee[0]
    if carte_jouee[1] == carte_meneuse[1] and carte_meneuse[1] != atout:
        if valeur_1==valeur_2 :
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
    else:
        if carte_jouee[1] == atout:
            if carte_meneuse[1] != atout:
                return -1
            else:
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
        else : 
            return 1
