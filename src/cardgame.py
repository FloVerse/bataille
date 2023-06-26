import random

class CardGame:
    def __init__(self):
        self.deck = []
        self.player1 = []
        self.player2 = []
        self.rounds = 0

    def create_deck(self):
        """
        Crée un jeu de 52 cartes mélangées.
        """
        values = list(range(2, 15))
        suits = ["Coeur", "Pique", "Trefle", "Carreau"]
        self.deck = [[value, suit] for value in values for suit in suits]
        random.shuffle(self.deck)

    def deal_cards(self):
        """
        Distribue les cartes du jeu aux deux joueurs.
        """
        self.player1 = self.deck[:26]
        self.player2 = self.deck[26:]

    def play_round(self):
        """
        Joue une manche de bataille.
        """
        card1 = self.player1.pop(0)
        card2 = self.player2.pop(0)

        print("Joueur 1:", card1)
        print("Joueur 2:", card2)

        if card1[0] > card2[0]:
            self.player1.append(card1)
            self.player1.append(card2)
            print("Joueur 1 remporte la manche.")
        elif card1[0] < card2[0]:
            self.player2.append(card1)
            self.player2.append(card2)
            print("Joueur 2 remporte la manche.")
        else:
            print("Égalité !")

        self.rounds += 1

    def play_game(self):
        """
        Joue une partie complète de bataille.
        """
        self.create_deck()
        self.deal_cards()
        print("Début de la partie de bataille !")
        print("==============================")
        while len(self.player1) > 0 and len(self.player2) > 0:
            random.shuffle(self.player1)
            random.shuffle(self.player2)
            print("\nManche", self.rounds + 1)
            print("--------------------")
            print("Joueur 1:", len(self.player1), "cartes")
            print("Joueur 2:", len(self.player2), "cartes")
            self.play_round()

        print("==============================")
        if len(self.player1) > len(self.player2):
            print("Joueur 1 remporte la partie !")
        elif len(self.player1) < len(self.player2):
            print("Joueur 2 remporte la partie !")
        else:
            print("La partie se termine par une égalité !")

# Exemple d'utilisation
game = CardGame()
game.play_game()
