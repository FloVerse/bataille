class Player:
    def __init__(self):
        self.main_deck = []
        self.reserve_deck = []
    def add_to_main_deck(self, cards):
        self.main_deck.extend(cards)
    def add_to_reserve_deck(self, cards):
        self.reserve_deck.extend(cards)