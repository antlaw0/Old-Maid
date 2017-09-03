import Card

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
                card = Card.Card(rank, suit)
                self.deck[rank + ' ' + suit] = card

    # def shuffle(self):
    #     # """A method tha shuffle the deck of cards"""
    #     random.shuffle(self.cards)

    def deal(self): #self, hands, card_per_hand=1):
        if len(self.deck) > 0:
            card = self.deck.popitem()
            return card
        else:
            print("No more cards to deal.")
        # # """A method that deal the cards to the hand. It accepts the list of hand and cards per hand """
        # for rounds in range(card_per_hand):
        #     for hand in hands:
        #         if self.cards:
        #             top_card = self.cards[0]
        #             self.give(top_card, hand)
        #         else:
        #             print("Can't continue deal. Out of cards!")



