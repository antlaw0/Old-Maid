class Hand(object):
    # "A hand of playing cards"
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            playingCards = ""
            for card in self.cards:
                playingCards += str(card) + " \t"
        else:
            playingCards = "There is no cards left to be played"
        return playingCards

    def clear(self):
        ## Im clearing all cards from hand
        self.cards = []

    def adding(self, card):
        self.cards.append(card)

    def giving(self, card, otherHand):
        # A distributing method
        otherHand.append(card)
        self.cards.remove(card)