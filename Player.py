class Player(object):
	
	def __init__(self, name,hand):
		self.name = name
		self.hand = hand
		self.pairs = []
	
		#credit to http://www.openbookproject.net/thinkcs/python/english2e/ch17.html
	def find_pairs(self):
		original_cards = self.hand.cards[:]
		for card in original_cards:
			match = card
			if match in self.hand.cards:
				self.hand.cards.remove(card)
				self.hand.cards.remove(match)
				self.pairs.append(card)