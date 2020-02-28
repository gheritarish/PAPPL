# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:32:08 2019

@author: alepe
"""
from Enchere import enchere

def distribution(paquet,joueur):
    """Fonction qui permet de distribuer un paquet mélangé aux joueurs. Prend en arguments un paquet mélangé et la liste des joueurs"""
    carte_1=[]
    carte_2=[]
    carte_3=[]
    carte_4=[]
    for i in range(20):
        if (i<3 or 12<=i<14):
            carte_1.append(paquet[i])
        elif (3<=i<6 or 14<=i<16):
            carte_2.append(paquet[i])
        elif (6<=i<9 or 16<=i<18):
            carte_3.append(paquet[i]) 
        elif (9<=i<12 or 16<=i<20):
            carte_4.append(paquet[i]) 
    carte_retournee=paquet[20]
    resultat=enchere(carte_1,carte_2,carte_3,carte_4,carte_retournee,joueur)
    if resultat=="On redistribue":
        return "On redistribue"
    else :
        preneur=resultat[0]
        if preneur ==0 :
            carte_1.append(paquet[20])
        elif preneur==1:
            carte_2.append(paquet[20])
        elif preneur==2:
            carte_3.append(paquet[20])
        elif preneur==3:
            carte_4.append(paquet[20])
        for i in range(21,32):
            if preneur==0:
                if (i<23):
                    carte_1.append(paquet[i])
                elif (23<=i<26):
                    carte_2.append(paquet[i])
                elif (26<=i<29):
                    carte_3.append(paquet[i]) 
                elif (29<=i<32):
                    carte_4.append(paquet[i]) 
            elif preneur ==1:
                if (i<24):
                    carte_1.append(paquet[i])
                elif (24<=i<26):
                    carte_2.append(paquet[i])
                elif (26<=i<29):
                    carte_3.append(paquet[i]) 
                elif (29<=i<32):
                    carte_4.append(paquet[i]) 
            elif preneur ==2:
                if (i<24):
                    carte_1.append(paquet[i])
                elif (24<=i<27):
                    carte_2.append(paquet[i])
                elif (27<=i<29):
                    carte_3.append(paquet[i]) 
                elif (29<=i<32):
                    carte_4.append(paquet[i]) 
            elif preneur ==3:
                if (i<24):
                    carte_1.append(paquet[i])
                elif (24<=i<27):
                    carte_2.append(paquet[i])
                elif (27<=i<30):
                    carte_3.append(paquet[i]) 
                elif (30<=i<32):
                    carte_4.append(paquet[i]) 
        return (carte_1,carte_2,carte_3,carte_4,resultat[1],resultat[0]) # On renvoie la liste dse cartes de chacun des joueurs, le joueur qui a pris et la couleur de l'atout
    
     
            
