from unittest import TestCase
from Player import Player
from Card_Class import Card
from DeckOfCards_Class import DeckOfCards
from unittest.mock import patch


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Ben", 26)
        self.deck = DeckOfCards()
        self.card = Card(2, 2)

    # init tests

    def test_init_valid_name_str(self):
        player1 = Player("Ben", 26)
        self.assertEqual(type(player1.name), str)
        self.assertTrue(player1.name, "Ben")

    def test_init_invalid_name_int(self):
        with self.assertRaises(TypeError):
            player = Player(5, 20)

    def test_init_valid_num_of_cards(self):
        player1 = Player("Ben", 9)
        player2 = Player("Ben", 10)
        player3 = Player("Ben", 26)
        player4 = Player("Ben", 27)
        self.assertEqual(player1.num_of_cards, 26)
        self.assertEqual(player2.num_of_cards, 10)
        self.assertEqual(player3.num_of_cards, 26)
        self.assertEqual(player4.num_of_cards, 26)
        self.assertTrue(type(player1.num_of_cards), int)

    def test_init_num_of_cards_between_10_to_26(self):
        player1 = Player("Ben", 11)
        player2 = Player("Ben", 25)
        self.assertEqual(player1.num_of_cards, 11)
        self.assertEqual(player2.num_of_cards, 25)

    # set_hand tests
    # חסר בדיקה של כל הקלפים בדיוק, שהועברו מהחבילה לשחקן בצורה תקינה לפי הסדר, ושיש קריאה לדיל וואן

    def test_set_hand_type_error(self):
        with self.assertRaises(TypeError):
            self.player.set_hand("DeckOfCards")

    def test_set_hand_valid_deck(self):
        self.player.set_hand(self.deck)
        for i in range(26):
            self.assertIsInstance(self.player.cards[i], Card)

    def test_set_hand_add_10_cards(self):
        player = Player("Ron", 10)
        player.set_hand(self.deck)
        for i in range(10):
            self.assertIsInstance(player.cards[i], Card)

    # get_card tests

    def test_get_card_from_a_full_deck(self):
        self.player.set_hand(self.deck)
        cards = self.player.cards.copy()
        self.assertIsInstance(self.player.get_card(), Card)  # check that get_card return a card
        self.assertEqual(self.player.cards, cards[:-1])  # check that the card was drawn get out from the end of player's hand

    @patch("builtins.print")
    def test_get_card_from_an_empty_deck(self, mock_print):
        self.assertEqual(None, self.player.get_card())
        mock_print.assert_called_with("No cards have left.")

    # add_card tests

    def test_add_card_invalid_type_error(self):
        with self.assertRaises(TypeError):
            self.player.add_card("Card")

    def test_add_card_valid(self):
        self.player.set_hand(self.deck)
        cards = self.player.cards.copy()  # Defining a copy of the original cards
        cards.insert(0, Card(2, 2))  # Adding manually the card to the top of the copy list
        self.player.add_card(Card(2, 2))  # Adding using the function "add_card"
        self.assertEqual(cards, self.player.cards)  # Comparing the lists to see if the function works

    def test_add_exist_card(self):
        self.player.set_hand(self.deck)
        with self.assertRaises(ValueError):
            self.player.add_card(self.player.cards[0])
            # this way is works too, probabilistically:
            # self.player.add_card(Card(1, 1))
            # self.player.add_card(Card(1, 2))
            # self.player.add_card(Card(1, 3))


