import Card2
import Deck
import Hand
import Player
import Computer

def main():
    deck = Deck.Deck()

    # drawnCard = deck.deal(5)
    # print(drawnCard)
    allPlayers = []

    allPlayers = makePlayer(1, allPlayers)
    allPlayers = makePlayer(2, allPlayers)
    allPlayers = dealOutCards(allPlayers, deck)

    while True:
        for player in allPlayers:
            player.find_pairs()
            input()

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
    deckLen = len(deck.deck)
    playersLen = len(players)
    cardsPerPlayer = int(deckLen / playersLen)
    extraCards = deckLen % playersLen

    for player in players:
        if extraCards > 0:
            deck.deal(player.hand, cardsPerPlayer + 1)
            extraCards -= 1
        else:
            deck.deal(player.hand, cardsPerPlayer)
    return players

main()
