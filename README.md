# PAPPL
L'objectif de ce projet d'application est de développer une intelligence artificielle pour un jeu de belote. La première étape est de permettre à plusieurs humains de jouer ensemble.

## Jeu avec plusieurs humains
Pour jouer entre plusieurs humains, nous procédons de la manière suivante : il faut lancer la fonction `partieDeBelote()`.

### Choix de partie
Au tout début, l'utilisateur se voit proposer un type de partie : à points ou nombre de donnes. Il précise alors quel type de partie il veut faire et le nombre de points qu'il veut fixer comme limite / le nombre de donnes à faire.

### Enchères
Chaque joueur rentre son nom (et rentre un nom différent, pour des raisons d'affichage). Puis, les deux joueurs entre qui se décide le tirage au sort pour décider qui commencera entrent leur nom. Le tirage au sort a lieu et le premier joueur peut alors choisir s'il veut prendre ou non. On tourne ainsi autour de la table.

Si aucun des 4 joueurs n'a pris, chaque joueur se voit offrir dans l'ordre la possibilité de prendre à une autre couleur, et seulement à une autre couleur puisqu'il doit choisir un atout différent.

### Jeu
Dès que quelqu'un a pris, le jeu commence. Chaque joueur joue sa carte et ce pour les 8 plis. Dès qu'un joueur entre une carte, le programme vérifie si le joueur est autorisé à jouer cette carte selon deux questions : est-ce que cette carte est dans son jeu ? Est-ce que les règles autorisent le joueur à jouer cette carte ? La première question permet d'empêcher les fautes de frappe et la seconde permet de vérifier que le joueur joue à la couleur fournie, monte à l'atout s'il peut, etc.

### Score
Après chaque donne, les scores sont calculés selon les plis faits par chaque équipe et la validation ou non du contrat (strictement plus de la moitié des points pour l'équipe preneuse). Puis, le joueur qui a commencé distribue, et ainsi de suite jusqu'à ce que la condition de fin de jeu soit atteinte.
