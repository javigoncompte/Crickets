#take two inputs
#have a parser dictionary
# 20x1 20x2 20x3 acceptablae inputs






def hit(player, CricketNumber, mult):

    
    counter = mult
    if CricketNumber in  player:
        hits = player[CricketNumber]
        if hits < 3:
          hits = counter + hits 
          player[CricketNumber] = hits
        else:
          player[CricketNumber] = 3

def checkifclosed(players, CricketNumber):
    player1 = players[0]
    player2 = players[1]

    if player1[CricketNumber] and player2[CricketNumber] == 3:
        print("number is closed")
        return(True)
    else:
      return(False)

def scores(player, CricketNumber, mult):
  if player[str(CricketNumber)] == 3:
      score = player['score']
      if score != 0:

        new_score = (score * int(mult)) + score
        player['score'] = new_score
      else:
        player['score'] = int(CricketNumber) * int(mult)
      

def showStatus(player):
        return(player)


# fucntions to have a hit 3 equals closed and compares both ones
#input being 20 x1(single double or tripple)
#score will work after value = 3 * the multiplier and add to score
def runCricket():
    Player_One = {
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 3,
        "bull": 0,
        "score": 0,
        "name": 'player_one'
    }


    Player_Two = {
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 3,
        "bull": 0,
        "score": 0,
        'name': 'player_2'
    }

    turnTitle = ["1st", "2nd", "3rd"]

    Players = [Player_One, Player_Two]
    for gameRound in range(20):
        for player in Players:
            print(player['name'] + " : Throw your darts!")
            print(" (ex) triple of 20 #=> 20x3 ")
            print(" (ex) inner bull #=> bullx2 ")
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
                            if checkifclosed(Players, res[0]) == True:
                                print("No points scored")
                                print("===")
                                print(showStatus(player))
                                break
                            else:
                              scores(player,res[0], int(res[1]))
                              hit(player, res[0], int(res[1]))
                                
                                
                                

                              print(showStatus(player))
                              break
                            

                        else:
                            print("try again cricketnumberx3(2)(1)")
                            break
                            
                    except:
                        print("Invalid value has been input!")
                        print("Try again : ", end="")



runCricket()