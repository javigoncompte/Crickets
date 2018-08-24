#take two inputs
#have a parser dictionary
# 20x1 20x2 20x3 acceptablae inputs
#if statement when a number is closed
#if statement when the opposite number is closed as well
#Statistics of numbers of Triple Throwed
# two dictionaries for each player with having scoreboard marks
import numpy as np


Player_1 = {
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0,
    "bull": 0
}


Player_2 = {
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0,
    "bull": 0
}


# fucntions to have a hit 3 equals closed and compares both ones
#input being 20 x1(single double or tripple)
#score will work after value = 3 * the multiplier and add to score

turnTitle = ["1st", "2nd", "3rd"]

Players = [Player_One, PLayer_Two]
for gameRound in range(20):
    for player in players:
        print(player + " : Throw your darts!")
        print(" (ex) triple of 20 #=> 20x3 ")
        print(" (ex) inner bull #=> bullseyex2 ")
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


                        break

                    else:
                        res = res.split("x")
                        cr.hit(name, res[0], int(res[1]))
                        print(cr.showStatus())
                        print("===")
                        if cr.chkFullMarkFinish(name):
                            print("Full mark finish!")
                            return(0)

                        cr.players[name].appendHistory(res[0], int(res[1]))
                        break

                except:
                    print("Invailed value has been input!")
                    print("Try again : ", end="")

class Cricket():
    def __init__(self, players):
        self.numOfPlayers = 2
        self.players = players

    def __Hit__(self, CricketNumber, mult):
        if CricketNumber in  self.players.keys():
            if counter = 3:
                self.player.values() = 3
            elif counter = 2:
                self.player.values() = 2
            elif counter = 1:
                self.players.values() = 1
            else:
                self.players.values() = 0
    def __CheckifClosed__(self):
