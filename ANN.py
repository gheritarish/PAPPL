# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:25:34 2020

@author: clegui
"""
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.preprocessing import LabelBinarizer # used for one-hot encoding
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error # compute MSE
from sklearn.metrics import accuracy_score

import random

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

# Any results you write to the current directory are saved as output.

from keras.models import Sequential
from keras.layers import Dense



DISCRETE_VALUES = 4
EPOCHS = 150
BATCH_SIZE = 64

df_raw = pd.read_csv('resultats_entrainement_ann_1er_pli.csv')
df_raw.head()

df_raw.columns


#features = ["duration","episodes", "genre", "source", "type", "score"]
#df_X = df_raw[features]
#df_X.shape
jeu1 = ["Cartes11","Cartes12","Cartes13","Cartes14","Cartes15","Cartes16","Cartes17","Cartes18"]
jeu2 = ["Cartes21","Cartes22","Cartes23","Cartes24","Cartes25","Cartes26","Cartes27","Cartes28"]
jeu3 = ["Cartes31","Cartes32","Cartes33","Cartes34","Cartes35","Cartes36","Cartes37","Cartes38"]
jeu4 = ["Cartes41","Cartes42","Cartes43","Cartes44","Cartes45","Cartes46","Cartes47","Cartes48"]

df_jeu1 = df_raw[jeu1]
df_jeu2 = df_raw[jeu2]
df_jeu3 = df_raw[jeu3]
df_jeu4 = df_raw[jeu4]

df_jeu1.head()

print(df_jeu1[:1])
jeu = df_jeu1[:1]
print(jeu.loc[0][0])
    

valeurs = [1,7,8,9,10]
figures = ["['Valet'","['Dame'","['Roi'"]
couleur = ["'pique']","'coeur']","'trèfle']","'carreau']"]
#on encode les valeurs 'Valet','Dame','Roi' 
#on encode les couleurs 'pique','coeur','trèfle','carreau'

##########

# one-hot encoding below
""" 
encoding = []
errors = 0
# encoder toutes les cartes du jeu
for i in range(len(df_jeu1)-1):
    main = df_jeu1[i:i+1]
    main1 = 
    for i in main:
        if i == 
    for j in figures:
        if j == 
    tokens = jeu1.Cartes11.iloc[i].split()


"""