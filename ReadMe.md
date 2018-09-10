# Crickets ScoreKeeper
Python 3.6.5

Pickle 3.0 (It has explicit support for bytes objects and cannot be unpickled by Python 2.x. This is the default protocol, and the recommended protocol when compatibility with other Python 3 versions is required)

Data was stored using Pickle into disk due to the serialization making the data streamed instead of being saved into a database
Since I consider these boards to be hashes with their own keys and represents
	Since the Data is not very demanding or big and it keeps states of the objects as the integrity of data is very important while the app is running
	but at the same time it needs to be reset every run of the application.
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
If evidence shows that the game rounds are too little a simple code change in gameRound can be done.

# Application Structure

The Application was structured in this way

- Define functions that are determined to be important to the game of Crickets

- Each of these Functions will either test the player boards to each other or just do mathematical equations to calculate score or number of hits

- There will be a function that will save a player object into Pickle to make it a serialized object into disk

- Each of the players will be saved into array which will make it a loop and take three turns each to hit darts where functions will apply.

- As well the player list will be saved in Disk using pickle.



# Run the python application on terminal


# Manual Tests Done

## Test if player numbers are closed for scoring
Set one of the players numbers to 20 and hit on the opposite players a 3x and plus 1x
will show closed number and no points

## Test if score is being calculated after the number is equal to 3

Set one of the Cricket numbers to 3 and input a 1x or 2x or 3x to see if score changed
As well hit a 3x on a number with 1 or 2 to see if number just adds up to 3
One test done was hit 19x2 then 19x2 it should be equal to 3  =  checked out

## Test if a unknown number is entered

Input of a non Cricket number but will still count since the board has other Numbers
Made for the input of non Cricket Numbers
