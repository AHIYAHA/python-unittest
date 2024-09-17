from unittest import TestCase, mock
from DeckOfCards_Class import DeckOfCards
from Card_Class import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_default(self):  # Test that checks the validity of the __init__ function
        self.assertEqual(self.deck.deck, [Card(value, suit) for suit in range(1, 5) for value in range(1, 14)])

    def test_init_no_equals_cards(self):  # Test that checks that there are no duplicates of the same card in the deck
        for card in self.deck.deck:
            self.deck.deck.remove(card)
            self.assertTrue(card not in self.deck.deck)

    def test_cards_shuffle(self):  # Test to check that after shuffle a normal deck and a mixed deck are not the same
        other_deck = DeckOfCards()
        self.deck.cards_shuffle()
        self.assertNotEqual(other_deck.deck, self.deck.deck)

    def test_deal_one_full_deck(self):  # Test that checks that the last card in the deck is dealt and removed
        cards = self.deck.deck.copy()
        self.assertIsInstance(self.deck.deal_one(), Card)
        self.assertEqual(self.deck.deck, cards[:-1])

    @mock.patch("builtins.print")  # Test that checks a message is printed when trying to deal a card from an empty deck
    def test_deal_one_empty_deck(self, mock_print):
        self.deck.deck = []
        self.assertEqual(None, self.deck.deal_one())
        mock_print.assert_called_with("Deck of cards is empty, there was not card drawn")


