from config import config
from partie import Partie
from equipe import Equipe
from joueur import Joueur
from paquet import Paquet
from interface import Interface
from tour import Tour
from manche import Manche


def main():
    # CONFIGURATION DE LA PARTIE
    partie, equipe1, equipe2 = config()

    # PAQUET MELANGE
    paquet = Paquet()
    paquet.melanger()

    # ORDRE DES JOUEURS
    partie.premier_joueur(paquet)

    # INTERFACE DE partie
    interface = Interface(partie.joueurs)

    score_additionnel = 0

    # PARTIE DE partie
    while partie.continuer(equipe1, equipe2):

        manche=Manche(score_additionnel)

        # ENCHERES
        while manche.enchere:
            # PAQUET MELANGE
            paquet = Paquet()
            paquet.melanger()

            # DISTRIBUTION DE 5 CARTES ET LA RETOURNE
            paquet.distribuer(partie.joueurs)

            # PREMIERE ENCHERE
            manche.encherir(partie.joueurs, interface, paquet.retourne)

            if manche.enchere:
                # DEUXIEME ENCHERE
                manche.encherir(partie.joueurs, interface, paquet.retourne, True)
        
        # DISTRIBUTION DES CARTES RESTANTES
        paquet.distribuer(partie.joueurs)

        # MANCHE DE partie
        for i in range(8):
            tour=Tour()

            for joueur in partie.joueurs:
                interface.positionne_noms(partie.joueurs, joueur)
                interface.positionne_cartes(joueur)
                tour.update(joueur.jouer(interface, partie.joueurs, tour, manche.atout), manche.atout)

            tour.gagnant_pli(partie.joueurs, manche.atout, equipe1, equipe2)
            partie.ordre_joueurs(tour.id_gagnant)
        
        equipe1.calcul_score(manche.atout, partie.joueurs[tour.id_gagnant].equipe==1)
        equipe2.calcul_score(manche.atout, partie.joueurs[tour.id_gagnant].equipe==2)
        score_additionnel = manche.resultat(equipe1, equipe2)
    
    print("Partie terminée")

if __name__ == "__main__":
    main()
