import os
import operator
from turn import Turn

def playerRefresh(players, n):
    newPlayers = {}
    for player in players.values():
        if player.purse > 0:
            newPlayers[player.playerNumber] = player
    if newPlayers:
        while True:
            if n == 1:
                newTurn = "y"
            else:
                newTurn = input("Do you want to keep playing (y/n)? ")
            if newTurn == "y":
                os.system('clear')
                return newPlayers
            elif newTurn == "n":
                print("Thank you for playing.\n\nFinal Leaderboard:\n")
                for player in (sorted(players.values(), key=operator.attrgetter('purse'), reverse=True)):
                    print(player)
                newPlayers = {}
                return newPlayers
    else:
        print("\nNo one has money.  GAME OVER!")
        newPlayers = {}
        return newPlayers