# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:37:10

@author: telmar
"""

def updateScore(score_act_eq1, score_act_eq2, gagne_eq1, gagne_eq2, eq_preneuse, belote):
    if eq_preneuse == 1:
        if gagne_eq1 >= 82 and gagne_eq1 > gagne_eq2:
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else:
            if belote in [0, 2]:
                if gagne_eq1 + 20 > gagne_eq2:
                    score_act_eq1 += gagne_eq1
                    score_act_eq2 += gagne_eq2
                else:
                    score_act_eq2 += 162
            else:
                score_act_eq2 += 162
    elif eq_preneuse == 2:
        if gagne_eq2 >= 82 and gagne_eq2 > gagne_eq1:
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else:
            if belote in [1, 3]:
                if gagne_eq2 + 20 > gagne_eq1:
                    score_act_eq2 += gagne_eq2
                    score_act_eq1 += gagne_eq1
                else:
                    score_act_eq1 += 162
            else:
                score_act_eq1 += 162
    
    if belote != 4:
        if belote in [0, 2]:
            score_act_eq1 += 20
        elif belote in [1, 3]:
            score_act_eq2 += 20
    return score_act_eq1, score_act_eq2
