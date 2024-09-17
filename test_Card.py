from unittest import TestCase
from Card_Class import Card


class TestCard(TestCase):
    # init:
    # valid value: 1,13
    # valid suit: 1,4
    # invalid value: 0, 14, not int
    # invalid suit: 0, 5, not int
    def test_init_valid(self):  # A test checks the correctness of the function when it receives valid values
        self.assertTrue(Card(1, 1))
        self.assertTrue(Card(13, 4))

    def test_init_valueError(self):  # Test to checks the function when receives invalid values and suits of a card
        with self.assertRaises(ValueError):
            card = Card(0, 1)  # Value can not be 0 (1 < value < 13)
        with self.assertRaises(ValueError):
            card = Card(14, 13)  # Value can not be 14 (1 < value < 13)
        with self.assertRaises(ValueError):
            card = Card(1, 5)  # Suit can not be 5 (1 < suit < 4)
        with self.assertRaises(ValueError):
            card = Card(13, 0)  # Suit can not be 0 (1 < suit < 4)

    def test_init_typeError(self):  # Test to checks the function when receives invalid type for values and suits
        with self.assertRaises(TypeError):
            card = Card(13, [0])  # Value/suit can't be a list (int only)
        with self.assertRaises(TypeError):
            card = Card({13}, 0)  # Value/suit can't be a dictionary (int only)

    # eq
    def test_eq_(self):
        with self.assertRaises(TypeError):
            boolean = 5 == Card(13, 1)

    # gt
    def test_gt_(self):
        with self.assertRaises(TypeError):
            boolean = 5 < Card(1, 1)  # Tests an error when a card is compared to an object that is not a card

    def test_gt_self_card_greater(self):  # Test to check if returns True when the value of the card is higher
        card1 = Card(10, 1)
        card2 = Card(5, 1)
        self.assertTrue(card1 > card2)

    def test_gt_other_card_greater(self):  # Test to check if returns False when the value of the other card is higher
        card1 = Card(5, 1)
        card2 = Card(10, 1)
        self.assertFalse(card1 > card2)

    def test_gt_cards_equal(self):  # Test to check if returns False when the cards are equal
        card1 = Card(10, 1)
        card2 = Card(10, 1)
        self.assertFalse(card1 > card2)

    def test_suit_comparison_self_greater(self):  # Test to check if returns True when the suit of the card is higher (while value is equal)
        card1 = Card(10, 3)
        card2 = Card(10, 1)
        self.assertTrue(card1 > card2)

    def test_suit_comparison_other_greater(self):  # Test to check if returns False when the suit of the other card is higher (while value is equal)
        card1 = Card(10, 1)
        card2 = Card(10, 3)
        self.assertFalse(card1 > card2)

    def test_self_is_ace(self):  # Test to check if returns True when the card is an Ace
        card1 = Card(1, 1)
        card2 = Card(2, 1)
        self.assertTrue(card1 > card2)

    def test_other_is_ace(self):   # Test to check if returns False when the other card is an Ace
        card1 = Card(2, 1)
        card2 = Card(1, 1)
        self.assertFalse(card1 > card2)

    def test_true_eq_(self):  # Test that returns True when two identical cards are compared
        card1 = Card(1, 1)
        card2 = Card(1, 1)
        self.assertTrue(card1 == card2)

    def test_false_eq_(self):  # Test that returns False when two different cards are compared
        card1 = Card(1, 2)
        card2 = Card(1, 1)
        self.assertFalse(card1 == card2)
