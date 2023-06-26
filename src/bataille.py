## Projet DUT2 Proba Poker
import math
import os
import numpy as np
import itertools
import random as rd
import math as m
from collections import Counter

## On stocke les cartes comme des listes d'un nombre et une chaine de caractère

# on utilise la correspondance Valet = 11, Dame=12, Roi = 13 et As= 14

VALUES = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "T", "V", "Q", "K", "A"]

# Si jamais vous souhaitez afficher les couleurs des cartes dans le terminal
COLORS = ["\u2665", "\u2660", "\u2663", "\u2666"]  # Hearts,Spades,Clubs,Diamonds

LIST_VALUES = list(range(2, 15))
LIST_COLORS = ["Coeur", "Pique", "Trefle", "Carreau"]

## Une carte est donc un élément ["valeur","couleur"]

LIST_NAME_HANDS = ["Carte Haute", "Paire", "Deux paires", "Brelan", "Suite", "Couleur", "Full", "Carré", "Quinte flush"]

### Création du jeu de 52 cartes
LIST_CARDS = []
for color in LIST_COLORS:
    for value in LIST_VALUES:
        LIST_CARDS.append([value, color])


def create_deck():
    """
    Création du jeu de 52 cartes
    :return: le jeu de 52 cartes
    """
    return LIST_CARDS

rd.shuffle(LIST_CARDS)
print(LIST_CARDS)
def get_hands() : 
    """
    Distribution d'un jeu de 52 cartes à 2 joueurs
    :return: les mains des 2 joueurs
    """
    return [LIST_CARDS[:26],LIST_CARDS[26:]]

print("------------------------------------")
print(get_hands()[0])