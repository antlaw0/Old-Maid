class Player(object):
	
	def __init__(self, name,hand):
		self.name = name
		self.hand = hand
		self.pairs = []
	
		#credit to http://www.openbookproject.net/thinkcs/python/english2e/ch17.html
	def find_pairs(self):
		original_cards = self.hand.cards[:]
		pairs_list=[]
		for card in original_cards:
			for card2 in original_cards:
				if card.suit != card2.suit and card.rank == card2.rank:
					print("pairs found:")
					print(card)
					print(card2)
					pairs_list.append(card)
					pairs_list.append(card2)
					#i=original_cards.index(card)
					#self.hand.cards.pop(i)
					#i=original_cards.index(card2)
					#self.hand.cards.pop(i)
		for c in self.hand.cards:
			for cc in pairs_list:
				if c.rank == cc.rank and c.suit == cc.suit:
					self.hand.cards.remove(c)
		"""
		for card in self.hand.cards:
			for card2 in self.hand.cards:
				if card != card2:
					if card.rank == card2.rank:
						pair = [card, card2]
						self.pairs.append(pair)
						self.hand.cards.remove(card)
						self.hand.cards.remove(card2)
"""