# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:37:10

@author: telmar
"""

def updateScore(score_act_eq1, score_act_eq2, gagne_eq1, gagne_eq2, eq_preneuse):
    if eq_preneuse == 1:
        if gagne_eq1 >= 82 and gagne_eq1 > gagne_eq2:
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else:
            score_act_eq2 += 162
    elif eq_preneuse == 2:
        if gagne_eq2 >= 82 and gagne_eq2 > gagne_eq1:
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else:
            score_act_eq1 += 162
    return score_act_eq1, score_act_eq2
