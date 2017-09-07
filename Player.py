class Player(object):

	def __init__(self, name, hand):
		self.name = name
		self.hand = hand
		self.pairs = 0

#	def find_pairs(self):
#		a=0
#		b=0
#		for i in self.hand.cards:
#			a=0
#			b=0
#			a+=1
#			for ii in self.hand.cards:
#				b+=1
#				if a != b:
#					if i.rank == ii.rank:
#						self.pairs.append(i)
#						self.hand.cards.remove(i)
#						self.hand.cards.remove(ii)
	def pairsInc(self):
		self.pairs=self.pairs+1



	def find_pairs(self):				#this method compares each card in the hand to every other card to look for matches and increments pairs when it finds one
		for i in self.hand:
			print("i is a ",type(i), " and it's value is, ",i)
			print("i's rank is:", i.getRank)
			for ii in self.hand:
				#print("ii is a ",type(ii), " and it's value is ",ii)
				if (i.getRank() == ii.getRank()) & (i !=ii) : #compare each card's rank with every other card in the hand's rank and make pair if rank matches and card doesn't (ie not the same card)
					#self.pairs =self.pairs+1
					self.pairsInc()
					self.hand.pop(i) #remove first half of pair TODO This line and next are trying to use value as key. needs to be fixed
					self.hand.pop(ii) #remove second half of pair
		print(self.name, " has ", self.pairs)

	def getPairs(self):
		return self.pairs

	def showHand(self):
		count=1
		for i in self.hand:
			print(str(count)+"\t"+str(i))
			count=count+1

	def passCard(self, player2, card):
		# A distributing method
		self.cards.remove(card)
		player2.add(card)