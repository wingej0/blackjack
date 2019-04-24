# A basic blackjack game for Python terminal
import operator
from player import Player
from turn import Turn

def main():
    numberOfPlayers = int(input("How many players (1-5)? "))
    players = {}
    if 1 <= numberOfPlayers <=5:
        i = 1
        while i <= numberOfPlayers:
            players[i] = Player(i)
            i += 1
    else:
        print("Try again!")

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
                Turn(newPlayers)
            elif newTurn == "n":
                print("Thank you for playing.\n\nFinal Leaderboard:\n")
                for player in (sorted(players.values(), key=operator.attrgetter('purse'), reverse=True)):
                    print(player)
                break
    else:
        print("\nNo one has money.  GAME OVER!")

main()