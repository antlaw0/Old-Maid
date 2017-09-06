class Player(object):
	
	def show_pairs(self):
		print("Pairs are: ")
		for i in self.pairs:
			print(i)
			
		
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
					self.pairs.append(card)
					self.pairs.append(card2)
					
		
		
		
		
		i=0
		for c in self.hand.cards:
			i=self.hand.cards.index(c)
			for cc in pairs_list:
				if c.rank == cc.rank and c.suit == cc.suit:
					self.hand.cards.pop(i)
		
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