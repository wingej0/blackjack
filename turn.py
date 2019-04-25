import os
import time
from deck import Deck
from hand import Hand
from total import total

def Turn(players):
    dealer = []
    hands = []
    # Create container list for each player
    for player in players.values():
        playerHand = Hand(player)
        hands.append(playerHand)
    
    # Deal the cards
    i = 1
    newDeck = Deck()
    while i <= 2:
        dealerCard = newDeck.draw()
        dealer.append(dealerCard)
        for hand in hands:
            playerCard = newDeck.draw()
            hand.hand.append(playerCard)
            hand.getTotal()
        i += 1
    dealerTotal = total(dealer)
    dealerShowCard = dealer[1].__str__()
    
    # Have each player bet and play
    for hand in hands:
        if hand.player.purse != 0:
            playerCards = [h.__str__() for h in hand.hand]
            print("\n" + hand.player.name + "'s turn:\n")
            print("The dealer shows a " + dealerShowCard + "\n")
            print("Your cards (Total = " + str(hand.total) + "):\n" + "\n".join(playerCards) + "\n")
            if hand.player.purse < 5:
                print("Your bet is $" + str(hand.player.purse) + "\n")
                hand.bet = hand.player.purse
            else:
                bet = 0
                while bet < 5 or bet > hand.player.purse:
                    try:
                        bet = int(input("What is your bet (between $5 - $" + str(hand.player.purse) + ")? "))
                        hand.bet = bet
                    except ValueError:
                        print("Your bet must be between $5 - $" + str(hand.player.purse))
            
            # Ask whether the player wants to hit or hold and act accordingly
            while True:
                actions = input("Do you want to hit or hold? ")
                if actions == "hit":
                    playerCard = newDeck.draw()
                    hand.hand.append(playerCard)
                    hand.getTotal()
                    newPlayerCards = [h.__str__() for h in hand.hand]
                    print("The dealer shows a " + dealerShowCard + "\n")
                    print("Your cards (Total = " + str(hand.total) + "):\n" + "\n".join(newPlayerCards) + "\n")
                    if hand.total > 21:
                        print("Bust")
                        break
                elif actions == "hold":
                    break

    # Dealer's turn
    dealerHand = [h.__str__() for h in dealer]
    print("Your total: " + str(hand.total))
    print("\nDealer's turn:\n" + "\n".join(dealerHand))
    time.sleep(1)
    while dealerTotal < 17:
        newDealerCard = newDeck.draw()
        dealer.append(newDealerCard)
        dealerTotal = total(dealer)
        print(newDealerCard)
        time.sleep(1)
    
    print("\nDealer total: " + str(dealerTotal))
    if dealerTotal > 21:
        print("The Dealer Busts.\n")
    else:
        print("The Dealer Holds.\n")
    
    # Print winners with updated purses
    for hand in hands:
        if hand.total > 21:
            newPurse = hand.player.loser(hand.bet)
            print(hand.player.name + " - Bust ($" + str(newPurse) + ")")
        elif dealerTotal > 21:
            newPurse = hand.player.winner(hand.bet)
            print(hand.player.name + " - Winner ($" + str(newPurse) + ")")
        elif hand.total > dealerTotal:
            newPurse = hand.player.winner(hand.bet)
            print(hand.player.name + " - Winner ($" + str(newPurse) + ")")
        elif hand.total < dealerTotal:
            newPurse = hand.player.loser(hand.bet)
            print(hand.player.name + " - Loser ($" + str(newPurse) + ")")
        else:
            newPurse = hand.player.push()
            print(hand.player.name + " - Push ($" + str(newPurse) + ")")
    
            

