# README
## Comment jouer
Pour jouer, tous les dossiers contiennent un fichier `Jeu.py`, qui contient deux uniques lignes, permettant de lancer une partie de belote. Ainsi, il suffit d'utiliser `python3.8 Jeu.py` depuis le dossier souhaité pour lancer une partie.

## Les différents fichiers
Comme expliqué précédemment, le fichier `Jeu.py` permet de jouer de manière simple.

Le fichier `PartieDeBelote.py` contient la fonction permettant de gérer une partie entière. C'est cette fonction qui est appelée par `Jeu.py`.

Le fichier `JeuDeLaCarte.py` est le fichier où est codée la fonction permettant de jouer une donne, c'est-à-dire de jouer les huit cartes du pli pour tous les joueurs. Cette fonction fait appel à la fonction `pli`, développée dans le fichier `Pli.py`, qui permet d'appeler la fonction correspondant au joueur. Ainsi, si le joueur est un humain, la fonction appelera la fonction `pliHumain`, développée dans le fichier `PliHumain.py` ; si le joueur est une IA naïve, la fonction `pliIA` du fichier `PliIA.py` sera appelée, et enfin si le joueur est une IA minimax, la fonction `pliIAMinimax` codée dans le fichier `PliIAMinimax.py` sera appelée.

Les fichiers `Minimax.py`, `JeuDeLaCarteMinimax.py` et `JeuDeLaCarteMinimaxInitialise.py` permettent de coder l'IA selon l'algorithme de minimax.

Les fichiers `CalculScore.py` et `UpdateScore.py` permettent de calculer le score de chacune des deux équipes après la partie et de mettre à jour le score global, en prenant en compte le contrat, la belote et, si besoin, un report de score sur la donne suivante.
