# Bataille.py
import random
from Player import Player


class Bataille:
    DECK_MIN_VALUE = 2
    DECK_MAX_VALUE = 15

    def __init__(self):
        self.deck = []
        self.played_cards = []
        self.player1 = Player()
        self.player2 = Player()
        self.rounds = 0

    def create_deck(self):
        """
        Crée un jeu de 52 cartes mélangées.
        """
        values = list(range(self.DECK_MIN_VALUE, self.DECK_MAX_VALUE))
        suits = ["Coeur", "Pique", "Trefle", "Carreau"]
        self.deck = [[value, suit] for value in values for suit in suits]
        random.shuffle(self.deck)

    def deal_cards(self):
        """
        Distribue les cartes du jeu aux deux joueurs.
        """
        # On choisit un joueur au hasard qui va recevoir la premiere carte
        starting_player = random.choice([self.player1, self.player2])
        for card in self.deck:
            starting_player.add_to_main_deck([card])
            starting_player = self.player1 if starting_player == self.player2 else self.player2

    def bataille(self, card1_played, card2_played):
        """
        Joue une bataille dans le cas d'une égalité
        """
        # Vérifie que les joueurs ont assez de cartes pour jouer une bataille, le cas échéant le joueur donne ses cartes
        if len(self.player1.main_deck) < 2:  # Joueur 1 n'a pas assez de cartes
            self.player2.add_to_reserve_deck([card1_played, card2_played])
            self.player2.add_to_reserve_deck(self.player1.main_deck)
            self.player1.main_deck.clear()
            return
        elif len(self.player2.main_deck) < 2:  # Joueur 2 n'a pas assez de cartes
            self.player1.add_to_reserve_deck([card1_played, card2_played])
            self.player1.add_to_reserve_deck(self.player2.main_deck)
            self.player2.main_deck.clear()
            return

        # Déroulement normal de la bataille

        # Une carte caché sur chaque deck
        card_hidden1 = self.player1.main_deck.pop(0)
        card_hidden2 = self.player2.main_deck.pop(0)
        # garder une trace des cartes jouées
        self.played_cards.extend([card1_played, card2_played, card_hidden1, card_hidden2])
        # On prend la deuxième carte visible de chaque joueur
        newCard1 = self.player1.main_deck.pop(0)
        newCard2 = self.player2.main_deck.pop(0)

        print("Joueur 1:", newCard1)
        print("Joueur 2:", newCard2)

        # Si joueur 1 gagne
        if newCard1[0] > newCard2[0]:
            self.player1.add_to_reserve_deck([newCard1, newCard2])
            self.player1.add_to_reserve_deck(self.played_cards)  # On ajoute les anciennes jouées à la réserve du joueur
            self.played_cards.clear() # On vide les cartes jouées
            print("Joueur 1 remporte la bataille.")
        # Si joueur 2 gagne
        elif newCard1[0] < newCard2[0]:
            self.player2.add_to_reserve_deck([newCard1, newCard2])
            self.player2.add_to_reserve_deck(self.played_cards)
            self.played_cards.clear()
            print("Joueur 2 remporte la bataille.")
        # Egalité
        else:
            print("Bataille !")
            self.bataille(newCard1, newCard2)


    def play_round(self):
        """
        Joue une manche de bataille.
        """
        # On prend la première carte de chaque joueur
        card1 = self.player1.main_deck.pop(0)
        card2 = self.player2.main_deck.pop(0)

        print("Joueur 1:", card1)
        print("Joueur 2:", card2)

        # Si joueur 1 gagne
        if card1[0] > card2[0]:
            self.player1.add_to_reserve_deck([card1, card2])
            print("Joueur 1 remporte la manche.")
        # Si joueur 2 gagne
        elif card1[0] < card2[0]:
            self.player2.add_to_reserve_deck([card1, card2])
            print("Joueur 2 remporte la manche.")
        # Egalité
        else:  # à traiter
            print("Bataille !")
            self.bataille(card1, card2)


        self.rounds += 1

    def run(self):
        """
        Joue une partie complète de bataille.
        """
        # On crée le jeu et on distribue les cartes
        self.create_deck()
        self.deal_cards()

        print("Début de la bataille !")
        print("==============================")
        while (len(self.player1.main_deck) + len(self.player1.reserve_deck)) > 0 and (
                len(self.player2.main_deck) + len(self.player2.reserve_deck)) > 0:
            print("\nManche", self.rounds + 1)
            print("--------------------")
            print("Joueur 1:", len(self.player1.main_deck), "cartes en jeu", "||",
                  "Joueur 2:", len(self.player2.main_deck), "cartes en jeu")

            print("Joueur 1:", len(self.player1.reserve_deck), "cartes en réserves", "||",
                  "Joueur 2:", len(self.player2.reserve_deck), "cartes en réserves")

            # On joue une manche
            self.play_round()
            # Si un joueur n'a plus de cartes mais qu'il a encore des cartes dans sa résérve
            if len(self.player1.main_deck) == 0 and len(self.player1.reserve_deck) > 0:
                self.player1.add_to_main_deck(self.player1.reserve_deck)
                self.player1.reserve_deck.clear()
                random.shuffle(self.player1.main_deck)
            if len(self.player2.main_deck) == 0 and len(self.player2.reserve_deck) > 0:
                self.player2.add_to_main_deck(self.player2.reserve_deck)
                self.player2.reserve_deck.clear()
                random.shuffle(self.player2.main_deck)

        print("==============================")
        if len(self.player1.main_deck) > len(self.player2.main_deck):
            print("Joueur 1 remporte la partie !")
        elif len(self.player1.main_deck) < len(self.player2.main_deck):
            print("Joueur 2 remporte la partie !")
        else:
            print("La partie se termine par une égalité !")
