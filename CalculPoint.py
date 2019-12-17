# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:19:35

@author: telmar
"""

def calculPoint(plis_eq1, plis_eq2, gagnant_der, atout, belote):
    """Cette fonction permetde calculer les scores des deux équipes. Elle prend deux listes de listes, plis_eq1 et plis_eq2, le gagnant du dernier pli, la couleur de l'autout, et le joueur qui a réalisé une belote (belote = 4 si personne ne l'a)"""
    points_eq1 = 0
    points_eq2 = 0
    equipe_belote = 0
    if plis_eq1 == []: # Dans le cas d'un capot de la part de l'équipe 2
        points_eq2 = 252
    elif plis_eq2 == []: # Dans le cas d'un capot de la part de l'équipe 1
        points_eq1 = 252
    else:
        for pli in plis_eq1: # On calcule les points de l'équipe 1, d'abord les plis dont les cartes valent toujours la même valeur, puis le valet et le 9 d'atout
            for carte in pli:
                if carte[0] == 1:
                    points_eq1 += 11
                elif carte[0] == 10:
                    points_eq1 += 10
                elif carte[0] == 'Roi':
                    points_eq1 += 4
                elif carte[0] == 'Dame':
                    points_eq1 += 3
                elif carte[0] == 'Valet':
                    if carte[1] == atout:
                        points_eq1 += 20
                    else:
                        points_eq1 += 2
                elif carte[0] == 9 and carte[1] == atout:
                    points_eq1 += 14
                else:
                    points_eq1 += 0
        for pli in plis_eq2: # On calcule les points de l'équipe22, d'abord les plis dont les cartes valent toujours la même valeur, puis le valet et le 9 d'atout
            for carte in pli:
                if carte[0] == 1:
                    points_eq2 += 11
                elif carte[0] == 10:
                    points_eq2 += 10
                elif carte[0] == 'Roi':
                    points_eq2 += 4
                elif carte[0] == 'Dame':
                    points_eq2 += 3
                elif carte[0] == 'Valet':
                    if carte[1] == atout:
                        points_eq2 += 20
                    else:
                        points_eq2 += 2
                elif carte[0] == 9 and carte[1] == atout:
                    points_eq2 += 14
                else:
                    points_eq2 += 0
        if gagnant_der in [0, 2]: # On termine par gérer les points du dernier pli
            points_eq1 += 10
        elif gagnant_der in [1, 3]:
            points_eq2 += 10
        if belote != 4: # Dans le cas où il y a belote, on ajoute les points à l'équipe concernée
            if belote in [0, 2]:
                points_eq1 += 20
                equipe_belote = 1
            elif belote in [1, 3]:
                points_eq2 += 20
                equipe_belote = 2
    return points_eq1, points_eq2, equipe_belote # On renvoie les points des deux équipes ainsi que l'équipe qui a réalisé une belote

