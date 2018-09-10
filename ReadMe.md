# Crickets ScoreKeeper
Python 3.6.5

Data was stored using Pickle into disk due to the serialization of it with python
	Since the Data is not very demanding or big and it keeps states of the objects 
# System settings
Cricket number x 3(2)(1) without spaces

Bullseye is 25 in this case

Only Two players

type "quit" to end the game

Example of Player Boards

```
Player_One = {
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 0,
        "25": 0,
        "score": 0,
        "name": 'player_one'} 
```
Another important system configuration is the implementation of set rounds to 20.
I consider 20 to be a normal number since it can't take non Cricket Numbers and 20 would be enough to have a closed game.
If evidence shows that the gamerounds are too little a simple code change in gameRound can be done.
    
# Run the python application on terminal


# Manual Tests Done

## Test if player numbers are closed for scoring
Set one of the players numbers to 20 and hit on the opposite players a 3x and plus 1x
will show closed number and no points

## Test if score is being calculated after the number is equal to 3

Set one of the Cricket numbers to 3 and input a 1x or 2x or 3x to see if score changed
As well hit a 3x on a number with 1 or 2 to see if number just adds up to 3

## Test if a unknown number is inputed

Input of a non Cricket number





