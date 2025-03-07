import pydealer
from collections import defaultdict
from player import Player
from helpers import printHand, getStackWinner
from constants import CARD_VALUES

class Round:
    
    
    
    def __init__(self):
        
        self.tarneeb = ""
        self.winningTeam: int
        self.bet = 6
        self.teamPoints: int
        self.hands = {}
        self.betWinningPlayer: Player
        self.teamPoints = {1: 0, 2: 0}
        self.offensiveTeam: int
        self.defensiveTeam: int


    def startBetting(self, players):
    

        playersStillBetting = [player for player in players if player.bettingStatus is True]

        while len(playersStillBetting) > 1 and self.bet < 13:
        
            for player in playersStillBetting:

                
                currBet = input(f"{player.name}, Please enter a bet greater than {self.bet} or pass:")

                if currBet.lower() == "pass":
                    player.bettingStatus = False
                    playersStillBetting = [player for player in players if player.bettingStatus is True]
                    if len(playersStillBetting) == 1:
                        break

                else:

                    self.bet = int(currBet)
                    self.betWinningPlayer = player
                    if self.bet == 13:
                        break

            print("\n\n")
            playersStillBetting = [player for player in players if player.bettingStatus is True]

        print(f"{self.betWinningPlayer.name}, you won the bet at {self.bet}")

        self.offensiveTeam = self.betWinningPlayer.team
        self.defensiveTeam = 0 if self.offensiveTeam is 1 else 1
        self.tarneeb = input("Please choose the neeb:")
        print("\n\n")


    def handoutCards(self, players):

        deck = pydealer.Deck()
        deck.shuffle()

        for player in players:

            player.hand = list(deck.deal(13))

        
    def playRound(self, players):

        playerDict = {player.id: player for player in players}
        playerHands = [len(player.hand) for player in players]

        currPlayingId = self.betWinningPlayer.id
        lastWinningPlayerId = self.betWinningPlayer.id
        
        while max(playerHands) > 0 and self.teamPoints[self.offensiveTeam] < self.bet and self.teamPoints[self.defensiveTeam] < (13 - self.bet + 1):
            
            tableSuit = ""
            tableStack = defaultdict(int)

            for i in range(4):
            
                print(f"\n{playerDict[currPlayingId].name}'s turn.")
                if tableSuit != "":
                    print(f"You must play a {tableSuit}")
                
                printHand(playerDict[currPlayingId].hand, "cols")

                playedCard = playerDict[currPlayingId].hand[int(input("Enter a value to play a card: "))]
                print(f"You played {playedCard}\n")
                tableStack[playedCard] = currPlayingId

                playerDict[currPlayingId].hand.remove(playedCard)

                for card in list(tableStack.keys()):
                    print(card)

                if lastWinningPlayerId == currPlayingId:
                    tableSuit = playedCard.suit

                
                if currPlayingId is 4:
                    currPlayingId = 1
                else:
                    currPlayingId += 1

            winningCard = getStackWinner(list(tableStack.keys()), tableSuit, self.tarneeb)
            lastWinningPlayerId = tableStack[winningCard]
            currPlayingId = lastWinningPlayerId

            print(f"Winner was {playerDict[lastWinningPlayerId].name} with the {winningCard}")

            tableStack = defaultdict(int)

            self.teamPoints[playerDict[lastWinningPlayerId].team] += 1

            print(f"Score")
            print(f"\tTeam 1: {self.teamPoints[1]}")
            print(f"\tTeam 2: {self.teamPoints[2]}")
            # empty table stack


            


