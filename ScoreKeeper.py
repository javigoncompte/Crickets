
def hit(player, CricketNumber, mult): #Counts number of hits and limit to 3
    counter = mult
    if CricketNumber in  player:
        hits = player[CricketNumber]
        if hits < 3:
            hits = counter + hits
            player[CricketNumber] = hits
        else:
            player[CricketNumber] = 3

def checkifclosed(players, CricketNumber): #Checks if the number is closed from other player
    player1 = players[0]
    player2 = players[1]
    if player1[CricketNumber] and player2[CricketNumber] == 3:
        print("number is closed")
        return(True)
    

def scores(player, CricketNumber, mult): #Handles scoring
  if player[str(CricketNumber)] == 3:
      score = player['score']
      if score != 0:
        new_score = (score * int(mult)) + score
        player['score'] = new_score
      else:
        player['score'] = int(CricketNumber) * int(mult)
      
def showStatus(player): #SHOW player board
        return(player)


#input being 20 x1(single double or tripple)
def runCricket():
    #25 will be the bullseye
    Player_One = {
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 0,
        "25": 0,
        "score": 0,
        "name": 'player_one'
    }


    Player_Two = {
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 0,
        "25": 0,
        "score": 0,
        'name': 'player_2'
    }

    turnTitle = ["1st", "2nd", "3rd"] #Turns for darts

    Players = [Player_One, Player_Two]
    for gameRound in range(20): #max 20 rounds estimate of how long the Cricket game would last
        for player in Players:
            print(player['name'] + " : Throw your darts!")
            print(" (ex) triple of 20 #=> 20x3 ")
            print(" (ex) inner bull #=> 25x2 ")
            print(" (ex) out of Cricket-Numbers #=> ")
            print(" (ex) Quit the Game #=> quit ")
            for i in turnTitle:
                print("player [" + player['name'] + "] " + i + " dart of round" +
                      str(gameRound + 1) + " : ", end="")

                while True:
                    try:
                        res = input()
                        
                        if res == "quit":
                            print("Quit the game!")
                            return(0)


                        elif 'x' in res:
                            res = res.split("x")
                            if checkifclosed(Players, res[0]):
                                print("No points scored")
                                print("===")
                                print(showStatus(player))
                                break
                            else:
                              scores(player, res[0], int(res[1]))
                              hit(player, res[0], int(res[1]))
                              print(showStatus(player))
                              break
                            

                        else:
                            print("try again cricketnumberx3(2)(1)")
                            break
                            
                    except:
                        print("Invalid value has been input!") #for errors
                        print("Try again : ", end="")
runCricket()