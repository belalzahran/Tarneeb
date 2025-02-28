# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import pydealer
import heapq
from collections import defaultdict



class Player:


    def __init__(self, name, id, team):
        self.name = name
        self.id = id
        self.team = team
        self.bettingStatus = True
        self.hand = []




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
            printHand(player.hand)
            print("\n\n")
        curr.startBetting(players)
        curr.playRound(players)

    
          
        
class Round:
    
    
    
    def __init__(self):
        
        self.tarneeb = ""
        self.winningTeam: int
        self.bet = 6
        self.bettingTeam: int
        self.hands = {}
        self.team1Points = 0
        self.team2Points = 0
        self.betWinningPlayer: Player


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

        self.bettingTeam = self.betWinningPlayer.team
        print(f"{self.betWinningPlayer.name}, you won the bet at {self.bet}")
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
        
        while max(playerHands) > 0:
            
            tableSuit = ""
            tableStack = defaultdict(int)

            for i in range(4):
            
                print(f"\n{playerDict[currPlayingId].name}'s turn.")
                if tableSuit != "":
                    print(f"You must play a {tableSuit}")
                
                printHand(playerDict[currPlayingId].hand)

                playedCard = playerDict[currPlayingId].hand[int(input("Enter a value to play a card: "))]
                print(f"You played {playedCard}\n")
                tableStack[playedCard] = currPlayingId

                playerDict[currPlayingId].hand.remove(playedCard)


                print(tableStack)

                if lastWinningPlayerId == currPlayingId:
                    tableSuit = playedCard.suit

                
                if currPlayingId is 4:
                    currPlayingId = 1
                else:
                    currPlayingId += 1

            winningCard = getStackWinner(list(tableStack.keys()), tableSuit, self.tarneeb)
            lastWinningPlayerId = tableStack[winningCard]

            print(f"Winner was {playerDict[lastWinningPlayerId].name} with the {winningCard}")

            tableStack = defaultdict(int)

            if playerDict[lastWinningPlayerId].team == 1:
                self.team1Points += 1
            else:
                self.team2Points += 1

            print(f"Score")
            print(f"\tTeam 1: {self.team1Points}")
            print(f"\tTeam 2: {self.team2Points}")
            # empty table stack


            







# HELPERS

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

    





def printHand(hand):

    for i, card in enumerate(hand):
        
        print(f"{i}. {card}")




CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 11, "Queen": 12, "King": 13, "Ace": 14  # Face cards mapped to numbers
}




    


            
            















players = [Player("BZ", 1, 1), Player("Saif", 2, 2), Player("BI", 3, 1), Player("Ali", 4, 2)]
        
        
newGame = Game()


newGame.playRound(players)













