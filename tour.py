class Tour():

    def __init__(self):
        self.pli = []
        self.id_maitre = 0
    
    def update(self, carte, atout):
        self.pli.append(carte)
        carte_maitresse=self.pli[self.id_maitre]
        carte_maitresse=carte_maitresse.compare(self.pli[-1], atout)
        for i, carte in enumerate(self.pli):
            if carte.nom==carte_maitresse.nom:
                self.id_maitre=i
                break

    def gagnant_pli(self, joueurs, equipe1, equipe2):
        gagnant=joueurs[id_maitre]
        if gagnant.equipe==1:
            equipe1.plis.append(self.pli)
        elif gagnant.equipe==2:
            equipe2.plis.append(self.pli)
        