import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card_ace = Card('spades', 1)
        self.card_4 = Card('spades', 4)
        self.card_jack = Card('hearts', 11)
        

    def test_card_is_an_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_ace))

    def test_jack_is_higher_than_4(self):
        higher_card = self.card_game.highest_card(self.card_4, self.card_jack)
        self.assertEqual(self.card_jack, higher_card)

    def test_card_total_is_16(self):
        cards = [self.card_ace, self.card_4, self.card_jack]
        self.assertEqual('You have a total of 16', self.card_game.cards_total(cards))
