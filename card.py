class Card(object):
    #A playing card
    def __init__(self, rank, suits):
        self.rank = rank
        self.suit = suits
        self.isFaceUp = False

    def __str__(self):
        if self.isFaceUp :
            display_card = self.rank + ' of ' + self.suit
        else:
            display_card = "Card face down"
        return display_card

    def flip(self):
        self.isFaceUp = not self.isFaceUp
