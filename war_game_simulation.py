"""
This is a simulation of a simplified version of the card game 'War'.
This program is a demonstration how Python OOP is used
and how classes can be connected to other classes not only trough inheritance.
"""

import random

# Definition of the deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    """
    A card class crates a Card object with three atributes: suit, rank and value
    """
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """
    A Deck is made of multiple Cards - the Deck class hold a list of Card objects,
    which mean's we will use the Card class within the __init__ of the Deck class.
    """
    def __init__(self):
        # This only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # We remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:
    """
    Player Class is able to hold instances of Cards, to remove or add them to the player.
    """
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # We remove one card from the list of all_cards
        # We state pop(0) to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        # adding multiple (list) cards (in case of winning war)
        if isinstance(new_cards, list): # better than type(new_cards) == type([])
            self.all_cards.extend(new_cards)
        # adding one card
        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# GAME SETUP

# Define Player 1 and 2
player_one = Player("One")
player_two = Player("Two")

# Create deck
new_deck = Deck()

# Shufle the deck
new_deck.shuffle()

# Deal the cards
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True


# THE GAME
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")
    print(f'Player 1 has {len(player_one.all_cards)} cards')
    print(f'Player 2 has {len(player_two.all_cards)} cards')

    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    # Otherwise, the game is still on!

    # Start a new round and put card on the table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        print(f'Player 1 draws {player_one_cards[-1]}')
        print(f'Player 2 draws {player_two_cards[-1]}')

        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')

            # First check to see if player has enough cards for war
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break

            # We're still at war, we add 5 cards on the table
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


