# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:21:23 2019

@author: alepe
"""

from PIL import Image
from resizeimage import resizeimage
 

TAILLE = [800, 700]
FIXE = 100
     
img = Image.open('aspique.PNG')
img = resizeimage.resize_height(img, FIXE)
img.save('height1.png', img.format)
    