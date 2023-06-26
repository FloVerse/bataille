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
for value in LIST_VALUES:
    for color in LIST_COLORS:
        LIST_CARDS.append([value, color])


### Création de la pioche
def get_remaining_card(used_cards):
    """
    Renvoie la liste des cartes restantes dans la pioche quand on a retiré l'ensemble used_card
    """
    M = LIST_CARDS.copy()
    for card in used_cards:
        M.remove(card)
    return M


### Fonctions à compléter

### Q1.2
def get_nb_colors(hand):
    """
    hand est un ensemble de 5 cartes
    Retourne le nombre de couleurs différentes dans la main
    """
    i = 0
    j = 0
    k = 0
    l = 0
    for value in range(len(hand)):
        if hand[value][1] == "Pique":
            if i < 1:
                i = i + 1
        if hand[value][1] == "Trefle":
            if j < 1:
                j = j + 1
        if hand[value][1] == "Coeur":
            if k < 1:
                k = k + 1
        if hand[value][1] == "Carreau":
            if l < 1:
                l = l + 1
    nc = i + j + k + l
    return nc

### Q1.3
def is_follows(hand):
    """
    hand est un ensemble de 5 cartes
    Retourne True si les 5 cartes se suivent et False sinon
    """
    hand.sort() # trie de la main
    #Il peut exitser une quinte "blanche" alors on peut vérifier
    if hand[0][0] ==2 and hand[1][0] == 3 and hand[2][0] == 4 and hand[3][0] == 5 and hand[4][0] == 14 :
        return True

    for carte in range(len(hand) - 1): # on parcourt la main
        if (hand[carte + 1][0] - hand[carte][0] != 1): # si la carte suivante - la carte actuelle est diffèrent de 1
            return False
    return True


### Q1.4
def get_hand_values(hand):
    """
    hand est un ensemble de 5 cartes
    Renvoie la valeur de la main
    """
    count = 0
    handValues = []
    three = 0  # compteur s'il ya  un trio
    pair = 0  # compteur pour s'il y a un pair

    for i in range(len(hand)):  # ici on créee une liste qui contient que les insignes des cartes.
        handValues.append(hand[i][0])

    for carte in range(len(hand)):  # on fait une boucle pour vérifier quelques apramètres
        # Full
        if handValues.count(
                hand[carte][0]) == 2:  # si la liste avec que les insignes contient 2 fois l'insigne de la amin
            count = count + 1  # compteur pour compter le nb cartes qu'il peut y avoir en  pair
            if pair < 1:  # pour que cela ne se fasse pas sur toutes les cartes
                pair = pair + 1
        if handValues.count(
                hand[carte][0]) == 3:  # si la liste avec que les insignes contient 3 fois l'insigne de la main
            if three < 1:  # pour que cela ne se fasse pas sur toutes les cartes
                three = three + 1  # on incrémente de 1
            # Carré
        if handValues.count(hand[carte][0]) == 4:
            return 7

    if three + pair == 2:  # si les incrémentations sont faites elles doivent valoir à 2 dans ce cas on retourne 6 car c'est un full
        return 6
        # Pair
    if pair == 1 and count < 4:  # nous avons deja verifier si pair était possible on non il vaut 1 si il est présent 0 sinon
        return 1

    # brelan
    if three == 1 and pair != 1:
        return 3
    # Quinte flush
    if is_follows(hand) and get_nb_colors(hand) == 1:
        return 8
        # Couleur
    if get_nb_colors(hand) == 1:
        return 5
        # Suite
    if is_follows(hand):
        return 4
    # deux paires
    if count == 4:
        return 2
    return 0



### Q1.5
def if_hand_values_are_equal(hand, other, same_value):
    """
    hand : une main (5 cartes)
    other : une autre main (5 cartes)
    N'utiliser cette fonction que si get_hand_values(hand) = get_hand_values(other) =same_value
    Retourne
        -- np.array([1,0,0]) si le joueur gagne
        -- np.array([0,0,1]) si le joueur perd
        -- np.array([0,1,0]) s'il y a égalité
    """

    local_hand = [0 for i in range(2, 15)]
    local_other = [0 for i in range(2, 15)]

    for i in range(5):
        local_hand[hand[i][0] - 2] += 1
        local_other[other[i][0] - 2] += 1

    local_hand.reverse()
    local_other.reverse()

    if same_value in [0, 4, 5, 8]:  # Pas de répétition de valeur
        if local_hand > local_other:
            return np.array([1, 0, 0])
        elif local_hand < local_other:
            return np.array([0, 0, 1])
        else:
            return np.array([0, 1, 0])

    elif same_value == 1:  # Une paire
        if local_hand.index(2) < local_other.index(2):
            return np.array([1, 0, 0])
        elif local_hand.index(2) > local_other.index(2):
            return np.array([0, 0, 1])
        else:
            local_hand.remove(2)
            local_other.remove(2)
            if local_hand > local_other:
                return np.array([1, 0, 0])
            elif local_hand < local_other:
                return np.array([0, 0, 1])
            else:
                return np.array([0, 1, 0])

    elif same_value == 2:  # 2 paires
        if local_hand.index(2) < local_other.index(2):
            return np.array([1, 0, 0])
        elif local_hand.index(2) > local_other.index(2):
            return np.array([0, 0, 1])
        else:
            local_hand.remove(2)
            local_other.remove(2)
            if local_hand.index(2) < local_other.index(2):
                return np.array([1, 0, 0])
            elif local_hand.index(2) > local_other.index(2):
                return np.array([0, 0, 1])
            else:
                if local_hand.index(1) < local_other.index(1):
                    return np.array([1, 0, 0])
                elif local_hand.index(1) > local_other.index(1):
                    return np.array([0, 0, 1])
                else:
                    return np.array([0, 1, 0])

    elif same_value in [3, 6]:  # Brelan , Full
        if local_hand.index(3) < local_other.index(3):
            return np.array([1, 0, 0])
        elif local_hand.index(3) > local_other.index(3):
            return np.array([0, 0, 1])
        else:
            local_hand.remove(3)
            local_other.remove(3)
            if local_hand > local_other:
                return np.array([1, 0, 0])
            elif local_hand < local_other:
                return np.array([0, 0, 1])
            else:
                return np.array([0, 1, 0])

    elif same_value == 7:  # 4 cartes de même valeur
        if local_hand.index(4) < local_other.index(4):
            return np.array([1, 0, 0])
        elif local_hand.index(4) > local_other.index(4):
            return np.array([0, 0, 1])
        else:
            if local_hand.index(1) < local_other.index(1):
                return np.array([1, 0, 0])
            elif local_hand.index(1) > local_other.index(1):
                return np.array([0, 0, 1])
            else:
                return np.array([0, 1, 0])
    else:
        print("ERROR")
        print(hand)
        print(other)
        print(LIST_NAME_HANDS[same_value])


def is_win(hand, other):
    """
    hand : une main (5 cartes)
    other : une autre main (5 cartes)
    Compare la main du joueur (hand)  avec la main de l'adversaire (other)
    Retourne
        -- np.array([1,0,0]) si le joueur gagne
        -- np.array([0,0,1]) si le joueur perd
        -- np.array([0,1,0]) s'il y a égalité
    """
    # À compléter
    win = np.array([1, 0, 0]) #gain
    lose = np.array([0, 0, 1]) #défaite
    if get_hand_values(hand) > get_hand_values(other): # si la valeur de la main du jouer est supèrieure à celle de l'adversaire
        return win
    elif get_hand_values(hand) == get_hand_values(other): # si c'est égale il faut retourner la fonction qui s'occupera de regarda laquelle est gagnante/perdante ou s'il ya vraiment égalité
        return if_hand_values_are_equal(hand, other, get_hand_values(hand))
    else: # si la valeur de la main de l'adversaire est supèrieure à celle du joueur
        return lose


### Q1.6
def get_best_hand(two_cards, table_cards):
    """
    two_cards : 2 cartes
    table_cards : 5 cartes
    Retourne la meilleur main possible dans les 7 cartes que sont les deux cartes du joueurs et les 5 cartes sur la table
    le cardinal de table_cards est de 5
    """
    handComplete = two_cards + table_cards #on prend toutes les cartes,,,,,,nnnnnnnnnnnnnnnnnnnnnnnnnnnn
    possibleHand = list(itertools.combinations(handComplete, 5)) # Cette fonction retourne toutes les valeurs possibles de 3 parmis 5 ce qui donne 10
    allPossibilities = [] #Cette liste contient toutes les cartes possibles non triée
    allHandPossibilities = [] #Cette liste contiendra toutes les mains possibles

    for tupl in possibleHand:   #itertools.combinations() renvoie un tuple, il faut donc le passer en forme de liste pour le manipuler
        for card in tupl:
            allPossibilities.append(card)

    for i in range(21):         #Création de la liste qui contiendra toutes les mains possibles
        allHandPossibilities.append([])

    hand = 0; #compteur des mains de toutes les possibilités
    while hand < 21: # On sait que 3 parmis 5 donne 10 il faut donc remplir le tableau avec 10 mains
        allHandPossibilities[hand].append(allPossibilities[0]) #Ajouts de toutes les possibilités de cartes dans la main
        allPossibilities.remove(allPossibilities[0])
        allHandPossibilities[hand].append(allPossibilities[0])
        allPossibilities.remove(allPossibilities[0])
        allHandPossibilities[hand].append(allPossibilities[0])
        allPossibilities.remove(allPossibilities[0])
        allHandPossibilities[hand].append(allPossibilities[0])
        allPossibilities.remove(allPossibilities[0])
        allHandPossibilities[hand].append(allPossibilities[0])
        allPossibilities.remove(allPossibilities[0])
        hand = hand + 1


    handFirst = allHandPossibilities[0] #On initialise une main
    for hand in allHandPossibilities:   #Pour toutes le smains possible nous alons regarder si la valeur est supérieure à la main que nous avons initialisé
        if get_hand_values(hand) > get_hand_values(handFirst): # si c'est le cas alors on la garde pour tester avec les prochaines
            handFirst = hand
        elif get_hand_values(hand) == get_hand_values(handFirst): # sinon si c'est la même valeur
           if if_hand_values_are_equal(hand,handFirst,get_hand_values(hand))[0] == 1 : # on utilise cette fonction pour voir qui gagne quand c'est la meme valeur
               handFirst = hand #si hand gagne alors hand devient handfirst
           else :
               handFirst = handFirst # sinon rien ne change


    bestHand = handFirst # la meilleure main devient handFirst

    return bestHand # On retourne la meilleure main



### Q1.7
def get_probabilities_after_flop(two_cards, flop):
    """
    two_cards : 2 cartes
    flop : 3 cartes
    Retourne un triplet
    np.array([proba de victoire, proba d'égalité, proba de défaite])
    après le flop (3 cartes)
    """
    win = 0 #initialisation des compteurs de victoire, défaite, et égalité
    lose = 0
    draw = 0
    possibleHand = list(itertools.combinations(get_remaining_card(flop+two_cards),2))  # Cette fonction retourne toutes les valeurs possibles de 2 parmis 47 ce qui donne 1081
    allPossibilities = []  # Cette liste contient toutes les cartes possibles non triée
    allHandPossibilities = []  # Cette liste contiendra toutes les mains possibles

    for tupl in possibleHand:  # itertools.combinations() renvoie un tuple, il faut donc le passer en forme de liste pour le manipuler
        for card in tupl:
            allPossibilities.append(card)
    for i in range(1081):  # Création de la liste qui contiendra toutes les mains possibles
        allHandPossibilities.append([])

    hand = 0; #compteur des mains de toutes les possibilités
    while hand < 1081: # On sait que 2 parmis 47 donne 1081 il faut donc remplir le tableau avec 1081 mains
        allHandPossibilities[hand].append(allPossibilities[0]) #Ajouts de toutes les possibilités de cartes dans la main
        allPossibilities.remove(allPossibilities[0])
        allHandPossibilities[hand].append(allPossibilities[0])
        allPossibilities.remove(allPossibilities[0])
        hand = hand + 1

    i = 0

    while i < 1081 :                            #On rentre dans le processus de compte
        print(round(((i * 100) / 1081)), "%")   #Création d'un pourcentage pour voir ou on en est dans le comptage
        flop.append(allHandPossibilities[i][0]) #on ajoute dans le flop une des 1081 possibilité de combinaisons
        flop.append(allHandPossibilities[i][1])
        possibleHand2 = list(itertools.combinations(get_remaining_card(flop+two_cards), 2))  # Cette fonction retourne toutes les valeurs possibles de 2 parmis 45 ce qui donne 990
        allPossibilities2 = []  # Cette liste contient toutes les cartes possibles non triée
        twoCardEnnemy = []  # Cette liste contiendra toutes les mains possibles

        for tupl in possibleHand2:  # itertools.combinations() renvoie un tuple, il faut donc le passer en forme de liste pour le manipuler
            for card in tupl:
                allPossibilities2.append(card)
        for j in range(990):  # Création de la liste qui contiendra toutes les mains possibles
            twoCardEnnemy.append([])

        
        c1 = 0;  # compteur des mains de toutes les possibilités
        while c1 < 990:  #dans cette boucle nous allons tester toutes le spossibilité de mains d'adversaire sur une main créee dans la boucle d'avant
            twoCardEnnemy[c1].append(allPossibilities2[0])  # Ajouts d'une possibilité dans la main de l'adversaire'
            allPossibilities2.remove(allPossibilities2[0])
            twoCardEnnemy[c1].append(allPossibilities2[0])
            allPossibilities2.remove(allPossibilities2[0])
            if is_win(get_best_hand(two_cards, flop), get_best_hand(twoCardEnnemy[c1], flop))[0] == 1: # si le joueur gagne
                win = win + 1
            elif is_win(get_best_hand(two_cards, flop), get_best_hand(twoCardEnnemy[c1], flop))[2] == 1: # si l'adrversaire gagne
                lose = lose + 1
            elif is_win(get_best_hand(two_cards, flop), get_best_hand(twoCardEnnemy[c1], flop))[1] == 1: # si égalité on utilisera la fonction qui renvoie l'issue
                if if_hand_values_are_equal(get_best_hand(two_cards, flop), get_best_hand(twoCardEnnemy[c1], flop), get_hand_values(get_best_hand(two_cards, flop)))[0] == 1:
                    win = win + 1
                elif if_hand_values_are_equal(get_best_hand(two_cards, flop), get_best_hand(twoCardEnnemy[c1], flop), get_hand_values(get_best_hand(two_cards, flop)))[1] == 1:
                    draw = draw + 1
                elif if_hand_values_are_equal(get_best_hand(two_cards, flop), get_best_hand(twoCardEnnemy[c1], flop), get_hand_values(get_best_hand(two_cards, flop)))[2] == 1:
                    lose = lose + 1

            c1 = c1 + 1 # on passe à la main de l'adversaire possible suivante

        flop.remove(flop[4]) # on supprime les deux cartes que nous avons ajoutés au flop
        flop.remove(flop[3])
        i= i+1 # on passe au 2 cartes en + du flop possible suivant

    proba_win = win/(1070190) #nb de victoires/defaites/égalité sur le nombre de possibilité totales 2 parmis 47 * 2 parmis 45
    proba_draw = draw/(1070190)
    proba_lose = lose/(1070190)


    return np.array([proba_win,proba_draw,proba_lose])



def get_probabilities_after_turn(two_cards, turn):
    """
    two_cards : 2 cartes
    turn : 4 cartes
    Retourne un triplet
    np.array([proba de victoire, proba d'égalité, proba de défaite])
    après le turn (4 cartes)
    """
    win = 0
    lose = 0
    draw = 0
    listCardLeft = get_remaining_card(turn+two_cards)
    #for card in LIST_CARDS:  # On doit récupérer le jeu de cartes sans les cartes qu'on connait déjà
        #if card == two_cards[0] or card == two_cards[1] or card == turn[0] or card == turn[1] or card == turn[2] or card == turn[3] :
            #listCardLeft.remove(card)
    count = 0
    print("Chargement : ")
    pr = round(((count * 100) / 1081))*22
    while count < 46 :
        if round(((count * 100) / 1081)*22) > pr :  #mise en place d'un pourcentage pour voir ou on en est
            print(round(((count * 100) / 1081)*22), "%")
            pr = round(((count * 100) / 1081)*22)
        turn.append(listCardLeft[count])
        listCardLeft2 = listCardLeft.copy()
        listCardLeft2.remove(listCardLeft[count])

        possibleHand = list(itertools.combinations(listCardLeft2,2))  # Cette fonction retourne toutes les valeurs possibles de 2 parmis 45 ce qui donne 990
        allPossibilities = []  # Cette liste contient toutes les cartes possibles non triée

        for tupl in possibleHand:  # itertools.combinations() renvoie un tuple, il faut donc le passer en forme de liste pour le manipuler
            for card in tupl:
                allPossibilities.append(card)

        tableCards = 0;  # compteur des mains de toutes les possibilités
        ennemyTwoCard = []
        while tableCards < 990:  # il faut tester avec les 990 possibilités de l'adversaire
            ennemyTwoCard.append(allPossibilities[0])  # Ajout d'une des possibilités de cartes dans la main
            allPossibilities.remove(allPossibilities[0])
            ennemyTwoCard.append(allPossibilities[0])
            allPossibilities.remove(allPossibilities[0])

            if is_win(get_best_hand(two_cards, turn), get_best_hand(ennemyTwoCard, turn))[0] == 1: # si le joueur gagne
                win = win + 1
            elif is_win(get_best_hand(two_cards, turn), get_best_hand(ennemyTwoCard, turn))[2] == 1: # si l'adversaire gagne
                lose = lose + 1
            elif is_win(get_best_hand(two_cards, turn), get_best_hand(ennemyTwoCard, turn))[1] == 1: # si égalité -> utiliser if_hand_values_are_equam
                if if_hand_values_are_equal(get_best_hand(two_cards, turn), get_best_hand(ennemyTwoCard, turn),get_hand_values(get_best_hand(two_cards, turn)))[0] == 1:
                    win = win + 1
                elif if_hand_values_are_equal(get_best_hand(two_cards, turn), get_best_hand(ennemyTwoCard, turn),get_hand_values(get_best_hand(two_cards, turn)))[1] == 1:
                    draw = draw + 1
                elif if_hand_values_are_equal(get_best_hand(two_cards, turn), get_best_hand(ennemyTwoCard, turn),get_hand_values(get_best_hand(two_cards, turn)))[2] == 1:
                    lose = lose + 1

            ennemyTwoCard.clear() #on clear la main de l'adversaire pour ajouté une autre possible main
            tableCards = tableCards + 1 # test de la prochaine possibilité de l'adversaire


        turn.remove(turn[4]) # quand on finit avec une possibilité de turn on la supprime
        count = count +1 # test de la porchiane possibilité de turn

    proba_win = win/(46*990) #nb de victoires/d"faite/égalité sur le nb de possibilité totales 1 parmis 46 * 2 parmis 45
    proba_lose = lose/(46*990)
    proba_draw = draw/(46*990)
    return np.array([proba_win,proba_draw,proba_lose])

def get_probabilities_after_river(two_cards, river):
    """
    two_cards : 2 cartes
    river : 5 cartes
    Retourne un triplet
    np.array([proba de victoire, proba d'égalité, proba de défaite])
    après la river (5 cartes)
    """
    listCardLeft = get_remaining_card(two_cards+river) #on récupère les cartes qu'on ne voit pas
    win = 0 # création des compteurs dans les situations de gain, echec ou égalité
    lose = 0
    draw = 0
    possibleHand = list(itertools.combinations(listCardLeft,2))  # Cette fonction retourne toutes les valeurs possibles de 2 parmis 45 ce qui donne 990
    allPossibilities = []  # Cette liste contient toutes les cartes possibles non triée
    allHandPossibilities = []  # Cette liste contiendra toutes les mains possibles

    for tupl in possibleHand:  # itertools.combinations() renvoie un tuple, il faut donc le passer en forme de liste pour le manipuler
        for card in tupl:
            allPossibilities.append(card)
    for i in range(m.comb(len(listCardLeft), 2)):  # Création de la liste qui contiendra toutes les mains de l'adversaire possibles
        allHandPossibilities.append([])

    courante = 0; #compteur des mains de toutes les possibilités
    while courante < m.comb(len(listCardLeft),2): # On sait que 2 parmis 45 donne 990 il faut donc tester avec 990 possibilité
        allHandPossibilities[courante].append(allPossibilities[0]) #Ajouts de toutes les possibilités de cartes dans la main
        allPossibilities.remove(allPossibilities[0])
        allHandPossibilities[courante].append(allPossibilities[0])
        allPossibilities.remove(allPossibilities[0])
        courante = courante + 1

    for hand in allHandPossibilities :  # Nous allons comparer toutes les meilleurs main possible de l'adversaire avec la meilleure main possible du joueur
        if is_win(get_best_hand(two_cards,river),get_best_hand(hand,river))[0] == 1 :
            win = win + 1
        elif  is_win(get_best_hand(two_cards,river),get_best_hand(hand,river))[2] == 1 :
            lose = lose +1
        elif is_win(get_best_hand(two_cards,river),get_best_hand(hand,river))[1] == 1 :
            if if_hand_values_are_equal(get_best_hand(two_cards,river),get_best_hand(hand,river),get_hand_values(get_best_hand(two_cards,river)))[0] == 1 :
                win = win +1
            elif if_hand_values_are_equal(get_best_hand(two_cards,river),get_best_hand(hand,river),get_hand_values(get_best_hand(two_cards,river)))[1] == 1 :
                draw = draw +1
            elif if_hand_values_are_equal(get_best_hand(two_cards,river),get_best_hand(hand,river),get_hand_values(get_best_hand(two_cards,river)))[2] == 1 :
                lose = lose +1

    # m.comb(len(listCardLeft),2) renvoie 2 parmis 45 donc  990
    proba_win = win/m.comb(len(listCardLeft),2)   #la proba se calcule donc en prenant le nb de fois qu'une situations apparait sur le nombre totals de possibilité
    proba_lose = lose/m.comb(len(listCardLeft),2)
    proba_draw = draw/m.comb(len(listCardLeft),2)
    return np.array([proba_win,proba_draw,proba_lose]) #on retourne un tableau







