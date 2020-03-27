class Equipe():

    def __init__(self, joueur1=None, joueur2=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.plis=[]
        self.der=False
        self.score_manche = 0
        self.score = 0
    
    def calcul_score(self, atout, der):
        self.score_manche=0
        if len(self.plis)==32:
            self.score_manche=252
        else:
            for pli in self.plis:
                for carte in pli:
                    if carte.valeur=="Valet" and carte.couleur==atout:
                        self.score_manche+=20
                    elif carte.valeur=="9" and carte.couleur==atout:
                        self.score_manche+=14
                    else:
                        self.score_manche+=carte.points
            if self.der:
                self.score_manche+=10
