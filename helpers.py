from collections import defaultdict
from constants import CARD_VALUES





def getStackWinner(cards, tableSuit, tarneeb):

    cardValues = defaultdict(int)
    

    for card in cards:

        card_value = CARD_VALUES.get(card.value, 0)

        if card.suit == tableSuit:
            cardValues[card] = card_value
        elif card.suit != tableSuit and card.suit != tarneeb:
            cardValues[card] = 0
        elif card.suit == tarneeb:
            cardValues[card] = card_value + 13

    maxValue = 0
    maxCard = None
    for card, value in cardValues.items():
        if value > maxValue:
            maxValue = value
            maxCard = card


    return maxCard

    




def printHand(hand, type):
    if type == "list":
        for i, card in enumerate(hand):
            print(f"{i}. {card}")
    else:
        suits = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}

        # Group cards by suit with their original indices
        for index, card in enumerate(hand):
            suits[card.suit].append((index, card))

        # Ensure each suit has 13 slots
        for suit in suits:
            while len(suits[suit]) < 13:
                suits[suit].append((None, None))

        # Print header
        column_width = 25  # Adjust to fit card names nicely
        header = f"{'Clubs'.ljust(column_width)}{'Diamonds'.ljust(column_width)}{'Hearts'.ljust(column_width)}{'Spades'.ljust(column_width)}"
        print(header)
        print("-" * (column_width * 4))

        # Print in columns
        for i in range(13):
            club = suits["Clubs"][i]
            diamond = suits["Diamonds"][i]
            heart = suits["Hearts"][i]
            spade = suits["Spades"][i]

            def format_card(card):
                return f"{card[0]}. {card[1]}" if card[0] is not None else ""

            row = f"{format_card(club).ljust(column_width)}{format_card(diamond).ljust(column_width)}{format_card(heart).ljust(column_width)}{format_card(spade).ljust(column_width)}"
            print(row)
