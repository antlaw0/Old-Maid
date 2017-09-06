class Player(object):

    playerCount = 0

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.pairs = []
        Player.playerCount += 1

    def find_pairs(self):
        original_cards = self.hand.cards[:]
        pairs_list = []
        for card in original_cards:
            for card2 in original_cards:
                if card.suit != card2.suit and card.rank == card2.rank:
                    # pair = [card, card2]
                    self.pairs.append(card)
                    self.pairs.append(card2)
                    pairs_list.append(card)
                    pairs_list.append(card2)
                    # self.hand.cards.remove(card)
                    # self.hand.cards.remove(card2)

        i = 0
        for c in self.pairs:
            for cc in self.hand.cards:
                i = self.hand.cards.index(cc)
                if c.rank == cc.rank and c.suit == cc.suit:
                    self.hand.cards.pop(i)

        print(self.pairs)
