# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:34:38 2019

@author: alepe
"""

def suppressionCartes(cartesRestantes, CartesDelete):
    for carte in CartesDelete :
        cartesRestantes.remove(carte)
    return cartesRestantes

