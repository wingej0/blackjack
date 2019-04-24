
def total(hand):
    total = 0
    # The cards have to be sorted so any aces are evaluated last
    cards = [h.getRank() for h in hand]
    cards.sort(reverse=True)
    for card in cards:
        if card in ["Ten", "Jack", "Queen", "King"]:
            cardValue = 10
        elif card == "Ace":
            if total < 11:
                cardValue = 11
            else:
                cardValue = 1
        else:
            cardValues = {
                "One" : 1,
                "Two" : 2,
                "Three" : 3,
                "Four" : 4,
                "Five" : 5,
                "Six" : 6,
                "Seven" : 7,
                "Eight" : 8,
                "Nine" : 9,
            }
            cardValue = cardValues[card]
        total += cardValue
    return total