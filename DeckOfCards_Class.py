from Card_Class import Card
from random import shuffle


class DeckOfCards:

    def __init__(self):  # This function creates a full deck of cards that contains 52 different cards

        self.deck = []

        for suit in range(1, 5):
            for value in range(1, 14):
                card = Card(value, suit)
                self.deck.append(card)

    def cards_shuffle(self):  # This function shuffles the cards
        shuffle(self.deck)

    def deal_one(self):  # This function takes a card from the deck (to use) and deletes it from the list
        if len(self.deck) > 0:
            return self.deck.pop()
        print("Deck of cards is empty, there was not card drawn")
