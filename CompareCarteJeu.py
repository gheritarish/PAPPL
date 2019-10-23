# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:30:35 2019

@author: telmar
"""

def compareCarteJeu(carte_meneuse, carte_jouee, atout):
	if carte_jouee[1] == carte_meneuse[1] and carte_meneuse[1] != atout:
		return compareCarte(carte_meneuse, carte_jouee)
	else:
		if carte_jouee[1] == atout:
			if carte_meneuse[1] != atout:
				return -1
			else:
				valeur_1 = carte_meneuse[0]
    			valeur_2 = carte_jouee[0]