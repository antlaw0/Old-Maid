class Player(object):

	def __init__(self, name,hand):
		self.name = name
		self.hand = hand
		self.pairs = []

	def find_pairs(self):
		a=0
		b=0
		for i in self.hand.cards:
			a=0
			b=0
			a+=1
			for ii in self.hand.cards:
				b+=1
				if a != b:
					if i.rank == ii.rank:
						self.pairs.append(i)
						self.hand.cards.remove(i)
						self.hand.cards.remove(ii)
						