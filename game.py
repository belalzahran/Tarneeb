

from round import Round
from player import Player

from helpers import printHand
from constants import CARD_VALUES


class Game:
    
    
    def __init__(self):
        self.team1Score = 0
        self.team2Score = 0
        self.roundsPlayed = 0
        self.rounds = []

    
    def playRound(self, players):

        curr = Round()
        curr.handoutCards(players)
        for player in players:
            player.hand.sort(key=lambda p: (p.suit, CARD_VALUES.get(p.value,0)))
            print(f"{player.name}'s Hand:")
            printHand(player.hand, "list")
            print("\n\n\n\n\n")
            printHand(player.hand, "col")
            print("\n\n")
        curr.startBetting(players)
        curr.playRound(players)
