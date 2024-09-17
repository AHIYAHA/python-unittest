from unittest import TestCase
from unittest.mock import patch
from Card_Class import Card
from CardGame import CardGame

#לא צריך לבדוק את האיניט יותר מפעם אחת, רק אם מספר הקלפים מתעדכן לפי הקלט. ובבדיקה של ניו גיים להוסיף מוקים, שהיא קוראת לפונקציות שהיא צריכה לקרוא להן, ובאיניט לוודא שהמצב שהיא אמורה לאתחל תקין, כל הקלפים הגיעו בצורה תקינה


class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("p1", "p2")

    # __init__ tests

    def test_init_sanity(self):
        """tests that the simple init (get 2 names) initializes all the features,
                so that every player has his name and full list with 26 cards, and the deck is empty"""

        # checking the features of first player
        self.assertEqual(self.game.player1.num_of_cards, 26)
        self.assertEqual(self.game.player1.name, "p1")
        for i in range(26):
            self.assertIsInstance(self.game.player1.cards[i], Card)

        # checking the features of second player
        self.assertEqual(self.game.player2.num_of_cards, 26)
        self.assertEqual(self.game.player2.name, "p2")
        for i in range(26):
            self.assertIsInstance(self.game.player2.cards[i], Card)

        # checking the deck is empty
        self.assertEqual(self.game.deck.deck, [])

    def test_init_invalid_name1(self):
        """tests raising error if the init method gets invalid name of the first player"""
        with self.assertRaises(TypeError):
            game = CardGame(5, "?")

    def test_init_invalid_name2(self):
        """tests raising error if the init method gets invalid name of the second player"""
        with self.assertRaises(TypeError):
            game = CardGame("5", 9)

    def test_init_invalid_num_of_cards(self):
        """tests the init method initializes all the features,
                also if it gets invalid num of cards,
                so that every player has his name and full list with 26 cards, and the deck is empty"""
        game = CardGame("p1", "p2", "p3")

        # checking the features of first player
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player1.name, "p1")
        for i in range(26):
            self.assertIsInstance(game.player1.cards[i], Card)

        # checking the features of second player
        self.assertEqual(game.player2.num_of_cards, 26)
        self.assertEqual(game.player2.name, "p2")
        for i in range(26):
            self.assertIsInstance(game.player2.cards[i], Card)

        # checking the deck is empty
        self.assertEqual(game.deck.deck, [])

    def test_init_high_num_of_cards(self):
        """tests the init method initializes all the features,
                if it gets num of cards higher than 26,
                then every player has his name and full list with 26 cards, and the deck is empty"""
        game = CardGame("p1", "p2", 27)

        # checking the features of first player
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player1.name, "p1")
        for i in range(26):
            self.assertIsInstance(game.player1.cards[i], Card)

        # checking the features of second player
        self.assertEqual(game.player2.num_of_cards, 26)
        self.assertEqual(game.player2.name, "p2")
        for i in range(26):
            self.assertIsInstance(game.player2.cards[i], Card)

        # checking the deck is empty
        self.assertEqual(game.deck.deck, [])

    def test_init_low_num_of_cards(self):
        """tests the init method initializes all the features,
                if it gets num of cards lower than 10,
                then every player has his name and full list with 26 cards, and the deck is empty"""

        game = CardGame("p1", "p2", 9)

        # checking the features of first player
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player1.name, "p1")
        for i in range(26):
            self.assertIsInstance(game.player1.cards[i], Card)

        # checking the features of second player
        self.assertEqual(game.player2.num_of_cards, 26)
        self.assertEqual(game.player2.name, "p2")
        for i in range(26):
            self.assertIsInstance(game.player2.cards[i], Card)

        # checking the deck is empty
        self.assertEqual(game.deck.deck, [])

    def test_init_26_num_of_cards(self):
        """tests the init method initializes all the features,
                if it gets num of cards exact 26,
                then every player has his name and full list with 26 cards, and the deck is empty"""

        game = CardGame("p1", "p2", 26)

        # checking the features of first player
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player1.name, "p1")
        for i in range(26):
            self.assertIsInstance(game.player1.cards[i], Card)

        # checking the features of second player
        self.assertEqual(game.player2.num_of_cards, 26)
        self.assertEqual(game.player2.name, "p2")
        for i in range(26):
            self.assertIsInstance(game.player2.cards[i], Card)

        # checking the deck is empty
        self.assertEqual(game.deck.deck, [])

    def test_init_10_num_of_cards(self):
        """tests the init method initializes all the features,
                if it gets num of cards 10,
                then every player has his name and full list with 10 cards, and the deck has the rest 32 cards"""

        game = CardGame("p1", "p2", 10)

        # checking the features of first player
        self.assertEqual(game.player1.num_of_cards, 10)
        self.assertEqual(game.player1.name, "p1")
        for i in range(10):
            self.assertIsInstance(game.player1.cards[i], Card)

        # checking the features of second player
        self.assertEqual(game.player2.num_of_cards, 10)
        self.assertEqual(game.player2.name, "p2")
        for i in range(10):
            self.assertIsInstance(game.player2.cards[i], Card)

        # checking the deck is empty
        for i in range(32):
            self.assertIsInstance(game.deck.deck[i], Card)

    @patch("game_cards.CardGame.CardGame.new_game")
    def test_if_init_calls_new_game(self, mock_new_game):
        """tests that the init method calls to new_game method and don't make new_game's work by itself"""
        game = CardGame("p1", "p2")
        game.new_game()
        mock_new_game.assert_called_once()

    # new_game test
    @patch("builtins.print")
    def test_new_game_during_the_game(self, mock_print):
        """tests that the new_game do nothing and print EM if it is called during the game"""
        cards1, cards2 = self.game.player1.cards.copy(), self.game.player2.cards.copy()  # before
        self.game.new_game()
        # after
        mock_print.assert_called_with("the game was started. impossible to begin a new game")
        self.assertEqual(cards1, self.game.player1.cards)
        self.assertEqual(cards2, self.game.player2.cards)

    # get_winner tests

    def test_get_winner_player1_win(self):
        del self.game.player2.cards[-1]
        self.assertEqual(self.game.get_winner(), self.game.player1)

    def test_get_winner_player2_win(self):
        del self.game.player1.cards[-1]
        self.assertEqual(self.game.get_winner(), self.game.player2)

    def test_get_winner_Tie(self):
        self.assertEqual(self.game.get_winner(), "Tie!")
