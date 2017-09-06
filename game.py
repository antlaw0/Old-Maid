import Card2
import Deck
import Hand
import Player
import Computer

def main():
    deck = Deck.Deck()
    print(deck)
    drawnCard = deck.deal(5)
    print(drawnCard)

hHand = Hand.Hand()
cHand = Hand.Hand()

# deck.deal([hHand, cHand], 20)
#
# human = Player.Player("Human", hHand)
# computer = Player.Player("AI", cHand)
# #print(computer.hand)
# #print(human.hand)
# loop = True
# human.find_pairs()
# print("before:")
# print(human.hand)
#
# print("pairs are: "+human.pairs[0].rank)
# print("after:")
# print(human.hand)

#while(loop == True):
	
main()