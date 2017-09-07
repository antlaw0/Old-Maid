import random
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
					pairs_list.append(card)
					pairs_list.append(card2)
					self.pairs.append(card)
					self.pairs.append(card2)
		
		i=0
		for c in pairs_list:
			for cc in self.hand.cards:
				i=self.hand.cards.index(cc)
				if c.rank == cc.rank and c.suit == cc.suit:
					self.hand.cards.pop(i)
					
	def get_random_card(self):
		r = random.randint(0,len(self.hand.cards)-1)
		c = self.hand.cards[r]
		return c
		