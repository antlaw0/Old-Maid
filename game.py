import Card
import Player

deck = Card.Deck()
deck.populate()
deck.shuffle()
hHand = Card.Hand()
cHand = Card.Hand()
deck.deal([hHand, cHand], 20)

human = Player.Player("Human", hHand)
computer = Player.Player("AI", cHand)
#print(computer.hand)
#print(human.hand)
loop = True
human.find_pairs()
print("before:")
print(human.hand)

print("pairs are: "+human.pairs[0].rank)
print("after:")
print(human.hand)

#while(loop == True):
	
