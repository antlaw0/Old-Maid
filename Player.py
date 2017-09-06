class Player(object):

    playerCount = 0

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.pairs = []
        Player.playerCount += 1

    def find_pairs(self):
        for card in self.hand:
            for card2 in self.hand:
                if card != card2:
                    if card.rank == card2.rank:
                        pair = [card, card2]
                        self.pairs.append(pair)
                        self.hand.cards.remove(card)
                        self.hand.cards.remove(card2)


                # a=0
                # b=0
                # for i in self.hand.cards:
                # 	a=0
                # 	b=0
                # 	a+=1
                # 	for ii in self.hand.cards:
                # 		b+=1
                # 		if a != b:
                # 			if i.rank == ii.rank:
                # 				self.pairs.append(i)
                # 				self.hand.cards.remove(i)
                # 				self.hand.cards.remove(ii)
						