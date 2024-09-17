class Card:

    def __init__(self, value: int, suit: int):  # This function gets the value and the suit of a card
        """class that contains a value and a suit of a card"""

        if int != type(value):  # raising an error if the value doesn't follow the conditions
            raise TypeError("Card value must be an integer")
        if 1 > value or value > 13:  # raising an error if the value doesn't follow the conditions
            raise ValueError("Card value must be between 1-13.")
        self.value = value

        if int != type(suit):  # raising an error if the suit doesn't follow the conditions
            raise TypeError("Card suit must be an integer.")
        if 1 > suit or suit > 4:  # raising an error if the suit doesn't follow the conditions
            raise ValueError("Card suit must be a number between 1-4.")
        self.suit = suit

    def __repr__(self):
        suit_symbols = {1: '♥', 2: '♣', 3: '♦', 4: '♠'}
        value_symbols = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

        suit_symbol = suit_symbols[self.suit]  # Replacing numeric values with suit symbols

        if self.value in value_symbols:
            value_symbol = value_symbols[self.value]  # Replacing numeric values with special value symbols
        else:
            value_symbol = self.value

        return f"({value_symbol} {suit_symbol})"

    def __gt__(self, other):  # Checks if the card value is greater than another
        if type(other) is not Card:  # raising an error if the suit doesn't follow the conditions
            raise TypeError("Card can be compared only to card")

        if self.value == other.value:  # If the cards values are the same then the def comparing the suits
            return self.suit > other.suit

        elif self.value == 1:
            return True

        elif other.value == 1:
            return False

        else:
            return self.value > other.value

    def __eq__(self, other):
        if type(other) is not Card:  # raising an error if the suit doesn't follow the conditions
            raise TypeError("Card can be compared only to card")

        return self.value == other.value and self.suit == other.suit
