
def black_jack(a, b, c):
    """
    Calculates the best possible blackjack hand value from three cards.
 
    Rules:
    - Sum the three card values.
    - If sum <= 21, return the sum.
    - If sum > 21 and one of the cards is an Ace (11), count the Ace as 1
      instead of 11 (subtract 10) and return the new total if it's <= 21.
    - Otherwise, the hand is a bust.
 
    Parameters:
        a (int): value of card 1 (Ace = 11, face cards = 10)
        b (int): value of card 2
        c (int): value of card 3
 
    Returns:
        int or str: hand total if <= 21, otherwise 'BUST'
    """
    total = a + b + c
 
    if total <= 21:
        return total
    elif total > 21 and 11 in (a, b, c):
        total -= 10
        return total if total <= 21 else 'BUST'
    else:
        return 'BUST'
 
 
if __name__ == "__main__":
    print(black_jack(9, 9, 11))   # Ace saves the hand -> 19
    print(black_jack(10, 10, 10)) # No ace -> BUST
    print(black_jack(5, 6, 7))    # Normal total -> 18
