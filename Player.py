from DeckOfCards_Class import DeckOfCards
from Card_Class import Card


class Player:
    def __init__(self, name: str, num_of_cards: int = 26):
        """initializes 3 features: name (given), num of cards (given or 26), cards (empty list, not given)"""
        if str != type(name):
            raise TypeError("Player name must be a word.")
        self.name = name

        if type(num_of_cards) is not int or num_of_cards < 10 or num_of_cards > 26:
            self.num_of_cards = 26
        else:
            self.num_of_cards = num_of_cards
        self.cards = []

    def set_hand(self, deck: DeckOfCards):
        """sets the first pack of cards of the player from the central shuffled deck of cards"""
        if type(deck) is not DeckOfCards:
            raise TypeError("the type of deck must be DeckOfCards")
        for i in range(self.num_of_cards):
            self.add_card(deck.deal_one())
# מה עם דיל וואן מחזיר נאן

    def get_card(self):
        """pops and returns the card that in the end of the pack of cards of the player"""
        if len(self.cards) == 0:
            print("No cards have left.")
        else:
            return self.cards.pop()

    def add_card(self, card: Card):
        """inserts a given card in the start of the pack of cards of the player"""
        if type(card) is not Card:
            raise TypeError("the type of card must be Card")
        if card in self.cards:
            raise ValueError(f"the card is already exist in the cards of {self.name}. cannot play with this deck, go to buy a new deck.")
        self.cards.insert(0, card)  # Adds a card in to index[0] of the players deck

    def __str__(self):
        """:return: a string describes the player, when his cards in table format, 6 cards in line"""
        cards = ""
        i = 0
        for card in self.cards:
            if i % 6 == 0:
                cards += "\n"
            else:
                cards += "\t"
            cards += str(card)
            i += 1

        return f"name: {self.name}, cards:{cards}"
