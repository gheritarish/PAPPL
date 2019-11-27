# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:37:10

@author: telmar
"""

def updateScore(score_act_eq1, score_act_eq2, gagne_eq1, gagne_eq2, eq_preneuse):
    """Permet de mettre à jour les points des deux équipes"""
    if eq_preneuse == 1: # Si l'équipe 1 a pris
        if gagne_eq1 >= 82 and gagne_eq1>gagne_eq2: # Si la condition de victoire est respectée
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else: # Sinon, l'autre équipe marque tous les points
            score_act_eq2 += 162
    elif eq_preneuse == 2: # Si l'équipe 2 a pris
        if gagne_eq2 >= 82 and gagne_eq2 > gagne_eq1: # Condition de victoire respectée
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else: # Ou l'autre équipe marque tous les points
            score_act_eq1 += 162
    return score_act_eq1, score_act_eq2
