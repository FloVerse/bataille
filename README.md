# Jeu de cartes - La bataille

Bienvenue dans le jeu de cartes "Bataille" ! 

C'est une implémentation simple du jeu de cartes classique utilisant Python.
Tout est généré aléatoirement, il n' y a pas de choix de l'utilisateur pour le moment.

## Régle du jeu de la bataille 


- On distribue les 52 cartes aux joueurs (la bataille se joue généralement à deux) qui les rassemblent face cachée en paquet devant eux.
- Chacun tire la carte du dessus de son paquet et la pose face visible sur la table.
- Celui qui a la carte la plus forte ramasse les autres cartes.
- L'as est la plus forte carte, puis roi, dame, valet, 10, etc.
- Lorsque deux joueurs posent en même temps deux cartes de même valeur il y a "bataille". 
- Le gagnant est celui qui remporte toutes les cartes du paquet.


#### Principe de la "Bataille"
Lorsqu'il y a "bataille" les joueurs tirent la carte suivante et la posent, face cachée, sur la carte précédente. Puis, ils tirent une deuxième carte qu'ils posent cette fois-ci face découverte et c'est cette dernière qui départagera les joueurs. Celui qui la valeur la plus forte, l'importe.

via [Wikipédia](https://fr.wikipedia.org/wiki/Bataille_(jeu))

## Classes

### Bataille
La classe `Bataille` est la classe principale du jeu. Elle contient les méthodes permettant de jouer une partie de bataille.

### Player
La classe `Player` permet de créer un joueur. Elle contient les méthodes permettant de gérer les cartes du joueur.

## Fonctionnalités

- Jeu de 52 cartes avec mélange aléatoire.
- Distribution équitable des cartes aux joueurs.
- Gestion de la "Bataille".
- Affichage des états du jeu après chaque manche.

## Fonctionnalités à venir
- Affichage graphique.
- Choix de l'utilisateur.
- Gestion des scores.