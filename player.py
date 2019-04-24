# Player class - Stores player number, name, and purse amount
class Player:
    def __init__(self, n):
        # Player number comes from the main function, asks for player name, and adds the purse
        self.playerNumber = n
        self.name = input("Player " + str(self.playerNumber) + "'s Name: ")
        self.purse = 100
    
    def winner(self, bet):
        self.purse += bet
        return self.purse
    
    def loser(self, bet):
        self.purse -= bet
        return self.purse
    
    def push(self):
        return self.purse
    
    def __str__(self):
        return "Player " + str(self.playerNumber) + ": " + self.name + " ($" + str(self.purse) + ")"

    def __repr__(self):
        return self.__str__()