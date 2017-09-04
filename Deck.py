import Card2

class Deck(object):
    # """ A deck of playing cards. """
    RANKS = ["Ace", "2", "3", "4", "5",
             "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    def __init__(self):
        self.deck = {}
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                card = Card2.Card(rank, suit)
                self.deck[rank + ' ' + suit] = card

    def deal(self, quantity = 1):
        while quantity > 0:
            if len(self.deck) > 0:
                card = self.deck.popitem()
                quantity -= 1
                return card
            else:
                print("No more cards to deal.")
                break
