# A basic blackjack game for Python terminal
from player import Player
from turn import Turn
from playerRefresh import playerRefresh

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
    n = 1
    while True:
        newPlayers = playerRefresh(players, n)
        if newPlayers:
            Turn(newPlayers)
            n += 1
        else:
            break

main()