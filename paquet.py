from carte import Carte
import random
from joueur import Joueur

class Paquet():

    def __init__(self):
        self.cartes = []
        valeur = ["1", "7", "8", "9", "10", 'Valet', 'Dame', 'Roi']
        points = [11, 0, 0,0,10,2,3,4]
        couleur = ['pique', 'coeur', 'trèfle', 'carreau']
        for i in range(len(valeur)):
            for j in range(len(couleur)):
                carte = Carte(valeur[i], couleur[j])
                self.cartes.append(carte)
        self.retourne = None

    def __str__(self):
        l = []
        for carte in self.cartes:
            l.append(carte.nom)
        return str(l)

    def melanger(self):
        nouveau_paquet = []
        longueur = len(self.cartes)
        for i in range(longueur):
            indice = random.randint(0, longueur-i-1)
            nouveau_paquet.append(self.cartes[indice])
            del self.cartes[indice]
        self.cartes = nouveau_paquet

    def distribuer(self, joueurs):
        if len(joueurs[0].cartes)==8 or len(joueurs[0].cartes)==0:
            for joueur in joueurs:
                joueur.cartes=[]
                joueur.pioche(self, 3)
            for joueur in joueurs:
                joueur.pioche(self, 2)
            self.retourne = self.cartes.pop()
        else:
            for joueur in joueurs:
                if joueur.preneur:
                    joueur.cartes.append(self.retourne)
                    joueur.pioche(self, 2)
                else:
                    joueur.pioche(self, 3)
