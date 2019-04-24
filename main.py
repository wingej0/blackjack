# A basic blackjack game for Python terminal
import os
import operator
from player import Player
from turn import Turn

def main():
    players = {}
    numberOfPlayers = 0
    while numberOfPlayers < 1 or numberOfPlayers > 5:
        try:
            numberOfPlayers = int(input("How many players (1-5)? "))
        except ValueError:
            print("Pick a number between 1-5.")
    
    i = 1
    while i <= numberOfPlayers:
        players[i] = Player(i)
        i += 1

    # Run a turn
    Turn(players)

    # After turn ask if they want to keep playing
    newPlayers = {}
    for player in players.values():
        if player.purse > 0:
            newPlayers[player.playerNumber] = player
    if newPlayers:
        while True:
            newTurn = input("Do you want to keep playing (y/n)? ")
            if newTurn == "y":
                os.system('clear')
                Turn(newPlayers)
            elif newTurn == "n":
                print("Thank you for playing.\n\nFinal Leaderboard:\n")
                for player in (sorted(players.values(), key=operator.attrgetter('purse'), reverse=True)):
                    print(player)
                break
    else:
        print("\nNo one has money.  GAME OVER!")

main()