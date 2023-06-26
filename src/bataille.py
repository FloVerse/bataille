import numpy as np
import random as rd
import math as m
from collections import Counter

class Bataille:
    def __init__(self):
        self.VALUES = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "T", "V", "Q", "K", "A"]
        self.COLORS = ["\u2665", "\u2660", "\u2663", "\u2666"]  # Hearts, Spades, Clubs, Diamonds
        self.LIST_VALUES = list(range(2, 15))
        self.LIST_COLORS = ["Coeur", "Pique", "Trefle", "Carreau"]
        self.LIST_NAME_HANDS = ["Carte Haute", "Paire", "Deux paires", "Brelan", "Suite", "Couleur", "Full", "Carré", "Quinte flush"]
        self.LIST_CARDS = []


    def create_deck(self):
        """
        Création du jeu de 52 cartes
        :return: le jeu de 52 cartes
        """
        for color in self.LIST_COLORS:
            for value in self.LIST_VALUES:
                self.LIST_CARDS.append([value, color])
        return self.LIST_CARDS

    def get_hands(self):
        """
        Distribution d'un jeu de 52 cartes à 2 joueurs
        :return: les mains des 2 joueurs
        """
        rd.shuffle(self.LIST_CARDS)
        deck1 = []
        deck2 = []
        for i in range(len(self.LIST_CARDS)):
            if i % 2 == 0:
                deck1.append(self.LIST_CARDS[i])
            else:
                deck2.append(self.LIST_CARDS[i])
        return [deck1, deck2]

    def is_win(self, OneCard, TwoCard):
        """
        Détermine si une carte est plus forte qu'une autre
        :param OneCard: la carte du joueur 1
        :param TwoCard: la carte du joueur 2
        :return: True si la carte du joueur 1 est plus forte que celle du joueur 2, False sinon
        """
        if OneCard[0] > TwoCard[0]:
            return True
        elif OneCard[0] < TwoCard[0]:
            return False
        elif OneCard[0] == TwoCard[0]:
            return True
