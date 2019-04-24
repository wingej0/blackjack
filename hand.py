# Hand class
from card import Card
from total import total

class Hand:
    def __init__(self, player):
        self.player = player
        self.hand = []
        self.total = 0
    
    def getTotal(self):
        self.total = total(self.hand)

    def __str__(self):
        return self.player.name + " - " + str(self.total)
    
    def __repr__(self):
        return self.__str__()