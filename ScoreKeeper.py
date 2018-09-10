#Pickle is going to be used to store Dictionaries into pickle files in disk
import pickle


def hit(player, CricketNumber, mult):
    #Counts number of hits and limit to 3
    # takes in player, Cricket Number and number of hits
    # counts to number of hits to each player in the score and sets a Number
    # assures that the hit hits 3 and it reaches 3 without going over

    counter = mult
    if CricketNumber in  player:
        hits = player[CricketNumber]
        if hits < 3:
            hits = counter + hits
            if hits > 3:
                player[CricketNumber] = 3
            else:
                player[CricketNumber] = hits
        else:
            player[CricketNumber] = 3

def checkifclosed(players, CricketNumber):
    #Function that will check if oppposite player has a closed Cricket number
    #Takes in a list of players and Circket Number
    # If player 1 hits a 3x and player two has 3 both players will show number closed
    # When player 1 hits 1x it will show number is closed and return True

    player1 = players[0]
    player2 = players[1]
    if player1[CricketNumber] and player2[CricketNumber] == 3:
        print("number is closed")
        return(True)


def scores(player, CricketNumber, mult):
    #Function will take in player, Cricket Number and (1,2,3) = multiplier  variables
    # The first logic will test if the players Cricket number has 3 hits so scoring can be allowed
    # if score does not equal 0 it will add score by getting current score and multiplying plus original score
    #  if score does not equal 0 it will make the math by getting the Cricket number * the multiplier

  if player[str(CricketNumber)] == 3:
      score = player['score']
      if score != 0:
        new_score = (score * int(mult)) + score
        player['score'] = new_score
      else:
        player['score'] = int(CricketNumber) * int(mult)

def showStatus(player):

    #SHOW player board and save player board
    #This function returns the board and saves the board after every action
    # "wb"  = open for writing, binary mode rb = reading binary

    pickle.dump(player, open("player.p", "wb"))


    return(player)


def runCricket():
    #input being 20 x1(single double or tripple)
    #25 will be the bullseye
    # First we will define the player boards
    Player_One = {
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 0,
        "25": 0, #bullseye
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
        "25": 0, #bullseye
        "score": 0,
        'name': 'player_2'
    }

    turnTitle = ["1st", "2nd", "3rd"] #Turntitles are the number of turns each player has

    Players_Array = [Player_One, Player_Two] # Set Players by making a list of Player1 and Player2

    #The idea of this was to store the players list into disk to avoid problems of memeory storage
    players = pickle.dump(Players_Array, open("players_list.p", "wb"))

    Players = pickle.load(open("players_list.p", "rb"))
    for gameRound in range(20): #The start of the game which is limited by 20(talked in the ReadMe as to why)
        for player in Players:

            # For each player we will do the following steps
            print(player['name'] + " : Throw your darts!")
            print(" (ex) triple of 20 #=> 20x3 ")
            print(" (ex) inner bull #=> 25x2 ")
            print(" (ex) out of Cricket-Numbers #=> ")
            print(" (ex) Quit the Game #=> quit ")


            for i in turnTitle:

                # for each Turn we will do

                print("player [" + player['name'] + "] " + i + " dart of round" +
                      str(gameRound + 1) + " : ", end="")

                while True: #If the While breaks it will will go to next round! or if quit returns false

                    try:
                        #First Test will be to verify the player wants to quit the most unprobable one
                        #Second Step will check if Cricket Number is Closed
                        #Third will do a score
                        # Give exceptions when user input error or invalid input
                        # Divide the input by x which will give us cricket number and multiplier
                        

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
