import Card2
import Deck
#import Hand
import Player
import random

#def main():
#    deck = Deck.Deck()
#    print(deck)
#    drawnCard = deck.deal()
#    print(drawnCard)
# hHand = Hand()
# cHand = Hand()
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
name=""
deck=Deck.Deck()

def humanTurn(human, computer,c):
    #code for human's turn
    print(human.name, ", it's your turn.")
    print("Your hand is: ")
    human.showHand()
    if c==0: #only ask this on the first turn.
        input("Type any key to automatically find all matches in your hand, remove them, and add them to your score.")
        human.find_pairs()
        print("You have ",human.getPairs(), " pairs so far.")
    else:
        comHandSize=computer.hand.cardsLeft()
        cardInd=input("Choose a card from my hand by typing a number between 1 and ", comHandSize,".")
        cIndex=(int(cardInd))-1
        card=computer.hand.cards[cIndex]
        computer.hand.giving(computer.hand, card, human.hand)
    print("Now your hand contains:")
    human.showHand()
    #the following line should have data validation added.
    match=input("If you have a pair, please type a to play your pair.  If you do not have a pair, type enter to pass your turn.")
    if match == 'a':
        human.find_pairs()
        print("You have ",human.getPairs(), " pairs so far.")
        return
    else: return

def computerTurn(computer, human, c):
    #code for computer's turn
    print("It's my turn.")
    if c==1:
        computer.find_pairs()
    else:
        humHandSize=human.hand.cardsLeft()
        cardInd=random.randint (0, (humHandSize-1))
        card=human.hand[cardInd]
        human.hand.giving(computer.hand, card, human.hand)
        computer.find_pairs()
        print("I have ", computer.getPairs(), " pairs so far.")

def main1():

    gameOn=input("Would you like to play Old Maid with me?  Type y for yes, anything else for exit")
    while gameOn=="y":
        print("My name is computer.")
        name=input("What is your name?")
        hand1=[]
        hand2=[]
        #hand1 = Hand.Hand
        #hand2 = Hand.Hand
        last = "h2"
        #while deck.cardsLeft()>0:
        #    if deck.cardsLeft():
        for i in range(53):
            c = deck.deal()
            #print("c is a ", type(c))
            if last == "h2":
    #                hand1.adding(hand1,c)
                hand1.append(c)
                last = "h1"
            elif last=="h1":
    #                hand2.adding(hand2,c)
                hand2.append(c)
                last = "h2"
        computer = Player.Player("Computer", hand2)
        human = Player.Player(name, hand1)

        turns=0
        prevTurn=computer
        if prevTurn==computer:
            humanTurn(human, computer, turns)
            prevTurn=human
            turns=turns+1
        else:
            computerTurn(computer, human, turns)
            prevTurn=computer
            turns=turns+1



        print("Here is your hand.")
        print(hand1)
        makePairs=input("would you like to match up and remove your cards automatically or would you prefer to make matches manually? Type a for automatically, and m for manually.")

        if makePairs=='a':
            Player.human.find_Pairs()

main1()