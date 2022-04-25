from mapGen import generateMap
from mineGen import generateMinefield
from playerMapFuncs import generatePlayerMap, playSpot, printPlayerMap, flagSpot

print("Hello and welcome to my text-based Minesweeper game developed as a simple project")
print("on my Python learning journey.")
print("The map will be a square matrix whose size will be defined by you, the player.")
print("The amount of mines will be 25% of the total map size rounded down.")
print("e.g. an 8x8 map will have 16 total mines.")
print("Maximum map size is 9x9 and minimum is 5x5. (Once I learn how to implement a graphic interface I will change the limitations, I promise.)\n")
print("Input desired map size: ")

mapSize = int(input())

while(mapSize < 5 or mapSize > 9):
        print("Map width cannot exceed 9 or be below 5.")
        print("Please input an allowed number: ")
        mapSize = int(input())

mineField = generateMap(mapSize)
mineField = generateMinefield(mineField)
playerMap = generatePlayerMap(mapSize)
mineCounter = [mapSize*mapSize*25//100]

printPlayerMap(playerMap, mineCounter)

gameRunning = True

while(gameRunning == True):

    print("To flag a spot type 'f', to play (clear) a spot type 'p'")
    choice = input()
    while(choice != "f" and choice != "p"):
        print("You're supposed to insert either 'f' to flag a spot or 'p' to play a spot right now. Nothing else.")
        choice = input()

    print("Insert a coordinate to play (vertical): ")
    yAxis = int(input())

    while(yAxis > mapSize or yAxis < 1 or yAxis == ""):
        print("Insert a VALID coordinate to play (vertical): ")
        yAxis = int(input())

    print("Insert a coordinate to play (horizontal): ")
    xAxis = int(input())

    while(xAxis > mapSize or xAxis < 1 or xAxis == ""):
        print("Insert a VALID coordinate to play (horizontal): ")
        xAxis = int(input())

    if(choice == "p"):
        playerMap = playSpot(xAxis, yAxis, mineField, playerMap)
    
    if(choice == "f"):
        playerMap = flagSpot(xAxis, yAxis, playerMap, mineCounter)
        mineCounter = playerMap[mapSize:]
        mineCounter = mineCounter[0]
        playerMap = playerMap[:-1]

    printPlayerMap(playerMap, mineCounter)
    if(playerMap[yAxis-1][xAxis-1] == "X"):
            print("Welp, it was a good run, but you're now scattered around a 10 meter radius area.")
            print("Try again? Maybe?")
            gameRunning = 0
    
    unknownsCounter = 0
    for i in range(mapSize):
        for j in range(mapSize):
            if (playerMap[i][j] == "?"): 
                unknownsCounter += 1
    
    if(unknownsCounter == 0):
        gameRunning = 0
        print("Great job! You've cleared this virtual minefield and made the area safe for children to play in!")
        print("You're a really wonderful person!")
        if(mapSize < 9):
            print("Why don't you try again on a bigger map?")
