import Card2
import Deck
import Hand
import Player
import Computer

def main():
    deck = Deck.Deck()
    print(deck)
    # drawnCard = deck.deal(5)
    # print(drawnCard)
    allPlayers = []

    allPlayers = makePlayer(1, allPlayers)
    allPlayers = makePlayer(2, allPlayers)
    dealOutCards(allPlayers, deck)

# deck.deal([hHand, cHand], 20)
#
#
#
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

def makePlayer(playerType, allPlayers):
    hand = Hand.Hand()
    if playerType == 1:
# TODO replace name with input.
        player = Player.Player("Human", hand)
    elif playerType == 2:
        player = Computer.Computer("Computer", hand)
    allPlayers.append(player)
    return allPlayers

def dealOutCards(players, deck):
    print("deck:" + str(len(deck.deck)) + " players:" + str(len(players)))
    cardsPerPlayer = int(len(deck.deck) / len(players))
    print(cardsPerPlayer)
    extraCards = len(deck.deck) % len(players)
main()