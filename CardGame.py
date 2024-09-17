from DeckOfCards_Class import DeckOfCards
from Player import Player


class CardGame:
    def __init__(self, p1_name, p2_name, num_of_cards=26):
        """initializes 3 features: 2 players and deck. in addition, calls the method new_game"""
        if type(num_of_cards) is not int or num_of_cards < 10 or num_of_cards > 26:
            num_of_cards = 26
        self.player1 = Player(p1_name, num_of_cards)
        self.player2 = Player(p2_name, num_of_cards)
        self.deck = DeckOfCards()
        self.new_game()

    def new_game(self):
        """shuffles the deck and set the two hands of the players in the beginning of the game.
        if activated during the game - print error message"""
        if len(self.deck.deck) == 52:
            self.deck.cards_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            print("the game was started. impossible to begin a new game")

    def get_winner(self):
        """:return: the player (object) with the big number of cards. if the players equal, return message (str)"""
        if len(self.player1.cards) > len(self.player2.cards):
            return self.player1
        if len(self.player2.cards) > len(self.player1.cards):
            return self.player2
        return "Tie!"

