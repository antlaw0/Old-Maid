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
    print("c is ", c)
    if c==0: #only ask this on the first turn.
        input("Type any key to automatically find all matches in your hand, remove them, and add them to your score.")
        human.find_pairs()
        human.find_pairs()
        human.find_pairs()
        print("You have ",human.getPairs(), " pairs so far.")
        print("line 42")
        print('cards left', len(human.hand))#correct so far
        return
    elif (c>0) & (len(computer.hand)>=1) & (len(human.hand)>=1):
        comHandSize=len(computer.hand)
        if len(computer.hand)!=0:
            cardInd=input("Choose a card from my hand by typing a number between 1 and "+ str( comHandSize)+".")
            cIndex=int(cardInd)-1
            card=computer.hand.cards[cIndex]
            computer.hand.giving(computer.hand, card, human.hand)
            print ('cards left', len(human.hand))
            print("Now your hand contains:")
            human.showHand()
            print("You have ", human.getPairs(), " pairs so far.")  # pairs correct here
            return
        else:return
    elif (len(computer.hand)<=1) & (len(human.hand)<=1):
        return

    #the following line should have data validation added.
#        match=input("If you have a pair, please type a to play your pair.  If you do not have a pair, type enter to pass your turn.")
 #   if match == 'a':
  #      human.find_pairs()
   # else: return

def computerTurn(computer, human):
    #code for computer's turn
    print("It's my turn.")
    p=computer.getPairs()
    if len(computer.hand)>2:
        computer.find_pairs()
        computer.find_pairs()
        computer.find_pairs()
        if computer.getPairs()>p:
            return
        else:
        #elif len(human.hand)>=1 & len(computer.hand)>=1:
            input("It's my turn to draw one of your cards.  Type enter to let me draw.")
            humHandSize=human.hand.cardsLeft()
            cardInd=random.randint (0, (humHandSize-1))
            card=human.hand[cardInd]
            human.hand.giving(computer.hand, card, human.hand)
            computer.find_pairs()
            print("I have ", computer.getPairs(), " pairs so far.")
    elif (len(computer.hand)<=1) & (len(human.hand)<=1):
        return

def win(computer, human):
    if (len(computer.hand)==1) & (len(human.hand)==0):
        print("I have the old maid.  You win.")
        return
    if (len(human.hand)==1) & (len(computer.hand) ==0):
        print("You have the old maid.  I win.")
        return





def main1():

    gameOn=input("Would you like to play Old Maid with me?  Type y for yes, anything else for exit")
    print("My name is computer.")
    name = input("What is your name?")
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
    cTurn=False
    count=0
    go=bool
    if gameOn=='y':
        go=True
    while go:

        if cTurn is False:
            print("trying to win", len(human.hand)," ", len(computer.hand))
            if (len(human.hand)==0) | (len(computer.hand)==0):
                win(computer,human)
                go=False

            else:
                humanTurn(human, computer, count)
                cTurn = True
                count=count+1
        elif cTurn is True:
            print("trying to win", len(human.hand), " ", len(computer.hand))
            if (len(human.hand)==0) | (len(computer.hand)==0):
                win(computer, human)
                go=False

            else:
                computerTurn(computer, human)
                cTurn = False
                count=count+1






#        print("Here is your hand.")
#        print(human.showHand())
#        makePairs=input("would you like to match up and remove your cards automatically or would you prefer to make matches manually? Type a for automatically, and m for manually.")

#        if makePairs=='a':
#            human.find_pairs()

main1()