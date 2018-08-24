#take two inputs
#have a parser dictionary
# 20x1 20x2 20x3 acceptablae inputs
#if statement when a number is closed
#if statement when the opposite number is closed as well
#Statistics of numbers of Triple Throwed
# two dictionaries for each player with having scoreboard marks
import numpy as np


Player_One = {
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0,
    "bull": 0,
    "score": 0
}


Player_Two = {
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0,
    "bull": 0,
    "score": 0
}


# fucntions to have a hit 3 equals closed and compares both ones
#input being 20 x1(single double or tripple)
#score will work after value = 3 * the multiplier and add to score

turnTitle = ["1st", "2nd", "3rd"]

Players = [Player_One, Player_Two]
cr = Cricket(Players)
for gameRound in range(20):
    for player in players:
        print(player + " : Throw your darts!")
        print(" (ex) triple of 20 #=> 20x3 ")
        print(" (ex) inner bull #=> bullx2 ")
        print(" (ex) out of Cricket-Numbers #=> ")
        print(" (ex) Quit the Game #=> quit ")
        for i in turnTitle:
            print("player [" + name + "] " + i + " dart of round" +
                  str(gameRound + 1) + " : ", end="")

            while True:
                try:
                    res = input()
                    if res == "quit":
                        print("Quit the game!")
                        return(0)

                    elif res == "":
                        res = res.split("x")
                        cr.hit(player, res[0], int(res[1]))
                        print("===")
                        break
                        if cr.checkifclosed(name):
                            print("Closed for Scoring")
                            return(0)
                        else:
                            cr.scores(player,(res[0], int(res[1]))

                    else:
                        print()
                except:
                    print("Invailed value has been input!")
                    print("Try again : ", end="")

class Cricket():
    def __init__(self, players):
        self.players = players


    def hit(self, CricketNumber, mult):

        for player in self.players:
            counter = mult
            if CricketNumber in  player.keys():
                if counter = 3:
                    player.values() = 3
                elif counter = 2:
                    player.values() = 2
                elif counter = 1:
                    player.values() = 1
                else:
                    player.values() = 0

    def checkifclosed(self, CricketNumber):
        player1 = self.players[0]
        player2 = self.players[1]
            if player1.items() & player2.items():
                return(True)
            else:
                return(False)

    def scores(self, CricketNumber, mult):
        for player in self.players:
            if player.values() == 3:
                score = player.get('score')
                new_score = (score * mult) + score
                player.update(score = new_score)
    def showStatus(self)
