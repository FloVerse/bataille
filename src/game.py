from bataille import Bataille
def run() : 
    bataille = Bataille()
    deck1 = []
    deck2 = []
    garbage1 = []
    garbage2 = []
    bataille.create_deck()
    deck1,deck2 = bataille.get_hands()
    while  len(deck1) < 52 and len(deck2) < 52:
        
        while len(deck1) > 0 and len(deck2) > 0:
            OneCard = deck1.pop(0)
            TwoCard = deck2.pop(0)
            if bataille.is_win(OneCard, TwoCard):
                garbage1.append(OneCard)
                garbage1.append(TwoCard)
            else:
                garbage2.append(OneCard)
                garbage2.append(TwoCard)
            
        deck1.append(garbage1)
        deck2.append(garbage2)
        
    if len(deck1) > 0:
        print("Joueur 1 gagne")
    else:    
        print("Joueur 2 gagne")



run()