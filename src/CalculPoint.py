# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:19:35

@author: telmar
"""

def calculPoint(plis_eq1, plis_eq2, gagnant_der, atout, belote):
    """Pour calculer les points de chacune des deux équipes"""
    points_eq1 = 0
    points_eq2 = 0
    if plis_eq1 == []:
        points_eq2 = 252
    elif plis_eq2 == []:
        points_eq1 = 252
    else:
        for pli in plis_eq1: # On compte les points de l'équipe 1
            for carte in pli:
                if carte[0] == 1:
                    points_eq1 += 11
                elif carte[0] == 10:
                    points_eq1 += 10
                elif carte[0] == 'Roi':
                    points_eq1 += 4
                elif carte[0] == 'Dame':
                    points_eq1 += 3
                elif carte[0] == 'Valet': # On sépare le valet d'atout des autres valets quand on compte les points
                    if carte[1] == atout:
                        points_eq1 += 20
                    else:
                        points_eq1 += 2
                elif carte[0] == 9 and carte[1] == atout: # On prend en compte le 9 d'atout
                    points_eq1 += 14
                else:
                    points_eq1 += 0
        for pli in plis_eq2: # On compte les points de l'équipe 2
            for carte in pli:
                if carte[0] == 1:
                    points_eq2 += 11
                elif carte[0] == 10:
                    points_eq2 += 10
                elif carte[0] == 'Roi':
                    points_eq2 += 4
                elif carte[0] == 'Dame':
                    points_eq2 += 3
                elif carte[0] == 'Valet': # On sépare le valet d'atout des autres valets quand on compte les points
                    if carte[1] == atout:
                        points_eq2 += 20
                    else:
                        points_eq2 += 2
                elif carte[0] == 9 and carte[1] == atout: # On prend en compte le 9 d'atout
                    points_eq2 += 14
                else:
                    points_eq2 += 0
        if gagnant_der in [0, 2]: # On compte ensuite les points du 10 de der selon l'équipe qui les remporte
            points_eq1 += 10
        elif gagnant_der in [1, 3]:
            points_eq2 += 10
        if belote != 4: # Si quelqu'un a fait belote et rebelote, on ajoute 20 points à l'équipe
            if belote in [0, 2]:
                points_eq1 += 20
            elif belote in [1, 3]:
                points_eq2 += 20
    return points_eq1, points_eq2

