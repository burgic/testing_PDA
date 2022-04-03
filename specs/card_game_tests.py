import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("hearts", "jack")

    def test_card_has_suit(self):
        self.assertEqual("hearts", self.card.suit)

    def test_card_has_value(self):
        self.assertEqual("jack", self.card.value)

    