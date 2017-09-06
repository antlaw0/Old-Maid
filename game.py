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

print("before:")
print(human.hand)
human.find_pairs()
print("after:")
print(human.hand)
human.show_pairs()


