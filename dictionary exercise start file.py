# This program uses a dictionary as a deck of cards.
import random

"""
def main():
    # Create a deck of cards.
    create_deck()

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))



    # Deal the cards.
    deal_cards()
"""


def ask_how_many_to_deal():
    """Returns the number of cards to deal between 1 and 52 per user prompt."""

    # Putting in a range tuple to make it easy to set the limits later
    range_to_deal = (1, 52)
    # Unpack the tuple into shorter names
    start, end = range_to_deal
    # Start with an invalid number of cards to deal so it enters loop
    cards_to_deal = 0

    # Loop until valid number in range is entered
    while cards_to_deal < start or cards_to_deal > end:
        # input() function returns a string, strip off any leading space
        deal_string = input(f"\nHow many cards should I deal [{start}-{end}]? ").strip()
        # if all the string characters are digits we can convert to int
        # without an exception occurring, just return it
        if deal_string.isdigit():
            cards_to_deal = int(deal_string)
            if cards_to_deal >= start and cards_to_deal <= end:
                return cards_to_deal
    # Should never get here but just in case return something
    # that will cause an exception
    return None


# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    return {
        "Ace of Spades": 1,
        "2 of Spades": 2,
        "3 of Spades": 3,
        "4 of Spades": 4,
        "5 of Spades": 5,
        "6 of Spades": 6,
        "7 of Spades": 7,
        "8 of Spades": 8,
        "9 of Spades": 9,
        "10 of Spades": 10,
        "Jack of Spades": 10,
        "Queen of Spades": 10,
        "King of Spades": 10,
        "Ace of Hearts": 1,
        "2 of Hearts": 2,
        "3 of Hearts": 3,
        "4 of Hearts": 4,
        "5 of Hearts": 5,
        "6 of Hearts": 6,
        "7 of Hearts": 7,
        "8 of Hearts": 8,
        "9 of Hearts": 9,
        "10 of Hearts": 10,
        "Jack of Hearts": 10,
        "Queen of Hearts": 10,
        "King of Hearts": 10,
        "Ace of Clubs": 1,
        "2 of Clubs": 2,
        "3 of Clubs": 3,
        "4 of Clubs": 4,
        "5 of Clubs": 5,
        "6 of Clubs": 6,
        "7 of Clubs": 7,
        "8 of Clubs": 8,
        "9 of Clubs": 9,
        "10 of Clubs": 10,
        "Jack of Clubs": 10,
        "Queen of Clubs": 10,
        "King of Clubs": 10,
        "Ace of Diamonds": 1,
        "2 of Diamonds": 2,
        "3 of Diamonds": 3,
        "4 of Diamonds": 4,
        "5 of Diamonds": 5,
        "6 of Diamonds": 6,
        "7 of Diamonds": 7,
        "8 of Diamonds": 8,
        "9 of Diamonds": 9,
        "10 of Diamonds": 10,
        "Jack of Diamonds": 10,
        "Queen of Diamonds": 10,
        "King of Diamonds": 10,
    }


# The deal_cards function deals a specified number of cards
# from the deck.


def deal_cards(deck, number):
    # Randomly create hand list by selecting cards from remaining deck cards
    # Normally you would use a {}.popitem() method but
    # it doesn't work properly so using a list instead
    # with function choice() from the random package
    hand = []
    remaining_deck = list(deck)
    while len(hand) < number:
        # Append a randomly chosen card from remaining cards in deck
        # Using the package random which must be imported the choice()
        # method returns a random entry from the list
        hand.append(random.choice(remaining_deck))
        # Remove returned card from reamining deck (card just appended)
        # This prevents hand duplicates
        remaining_deck.remove(hand[-1])

    # Display the cards in the hand list
    print()
    hand_value = 0
    for card in hand:
        print(card)
        # Deck is a dictionary with card as key and hand value as value
        # Sum the values after printing each card in the hand list
        hand_value += deck[card]

    # Display the accumulated hand value
    print(f"\nValue of this hand: {hand_value}\n")


# Main code
if __name__ == "__main__":
    deal_cards(create_deck(), ask_how_many_to_deal())
