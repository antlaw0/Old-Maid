from Player import Player


class Computer(Player):

    computerCount = 1

    def __init__(self, name, hand):
        Player.__init__(self, name + str(Computer.computerCount), hand)

        print(self.name)
        Computer.computerCount += 1
