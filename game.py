import Card
import Player

deck = Card.Deck()
deck.populate()
deck.shuffle()
hHand = Card.Hand()
cHand = Card.Hand()
deck.deal([hHand, cHand], 25)

human = Player.Player("Human", hHand)
computer = Player.Player("AI", cHand)
#print(computer.hand)
#print(human.hand)
loop = True

#print("before:")
#print(human.hand)
#human.find_pairs()
#print("after:")
#print(human.hand)
#human.show_pairs()

print("Welcome to Old Maid")
	

while(loop == True):
	computer.find_pairs()
	human.find_pairs()
	print("Your turn")
	print("Your hand is: ")
	print(human.hand)
	print("Your pairs are: ")
	human.show_pairs()
	print("You take a card from computer")
	c = human.get_random_card()
	print("You give computer a "+c.rank+" of "+c.suit)
	human.hand.give(c, computer.hand)
	
	
	print("Computer's turn")
	computer.find_pairs()
	print("Computer takes a card from you")
	c = computer.get_random_card()
	print("Computer gives you a "+c.rank+" of "+c.suit)
	computer.hand.give(c, human.hand)
	
	if len(human.hand.cards) == 1:
		print("You lose")
	if len(computer.hand.cards) == 1:
		print("Computer loses")

