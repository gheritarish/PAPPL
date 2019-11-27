# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:37:10

@author: telmar
"""

def updateScore(score_act_eq1, score_act_eq2, gagne_eq1, gagne_eq2, eq_preneuse, equipe_belote, score_reporte):
    if gagne_eq1 == gagne_eq2: # En cas d'égalité des points, on reporte les points de l'équipe preneuse à la partie suivante et l'autre équipe marque ses points
        score_reporte += gagne_eq1
        if eq_preneuse == 1:
            score_act_eq2 += gagne_eq2
        elif eq_preneuse == 2:
            score_act_eq1 += gagne_eq1
    if eq_preneuse == 1:
        if gagne_eq1 >= 82 and gagne_eq1>gagne_eq2:
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else:
            score_act_eq2 += 162
            if equipe_belote == 1:
                score_act_eq1 += 20 # On marque toujours les points de la belote
            elif equipe_belote == 2:
                score_act_eq2 += 20
    elif eq_preneuse == 2:
        if gagne_eq2 >= 82 and gagne_eq2 > gagne_eq1:
            score_act_eq1 += gagne_eq1
            score_act_eq2 += gagne_eq2
        else:
            score_act_eq1 += 162
            if equipe_belote == 1:
                score_act_eq1 += 20
            elif equipe_belote == 2:
                score_act_eq2 += 20
    return score_act_eq1, score_act_eq2, score_reporte
