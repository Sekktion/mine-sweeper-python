def generatePlayerMap(mapSize):

    playMap = []
    row = []
    for i in range(0,mapSize):
        for j in range(0,mapSize):
            row.append("?")
        playMap.append(row)
        row = []

    return playMap


def playSpot(xAxis, yAxis, mineField, playerMap):

    width = len(mineField)
    
    if(playerMap[yAxis-1][xAxis-1] == "F"):
        print("Can't play a flagged spot, try another one.")
        return playerMap

    if(mineField[yAxis-1][xAxis-1] == "X"):
        playerMap[yAxis-1][xAxis-1] = "X"
        return playerMap

    if(yAxis-2 < 0): #In case the inserted Y is on the upper limit of the board
        if(xAxis-2 < 0): #In case the inseted X is on the left most point of the board
            mineCounter = i = j = 0
            for i in range(2):
                for j in range(2):
                    if(mineField[yAxis-i][xAxis-j] == "X"):
                        mineCounter += 1
                    j += 1
                j = 0
                i += 1
            playerMap[yAxis-1][xAxis-1] = mineCounter
            return playerMap

        if(xAxis > width-1): #In case the inserted X is on the right most point of the board
            mineCounter = i = j = 0
            for i in range(2):
                for j in range(2):
                    if(mineField[yAxis-i][xAxis-1-j] == "X"):
                        mineCounter += 1
                    j += 1
                j = 0
                i += 1
            playerMap[yAxis-1][xAxis-1] = mineCounter
            return playerMap
        
        mineCounter = i = j = 0
        for i in range(2):
            for j in range(3):
                if(mineField[yAxis-i][xAxis-j] == "X"):
                    mineCounter += 1
                j += 1
            j = 0
            i += 1
        playerMap[yAxis-1][xAxis-1] = mineCounter
        return playerMap

    if(yAxis > width-1): #IN case the inserted Y is on the lower limit of the board
        if(xAxis-2 < 0): #In case the inseted X is on the left most point of the board
            mineCounter = i = j = 0
            for i in range(2):
                for j in range(2):
                    if(mineField[yAxis-1-i][xAxis-j] == "X"):
                        mineCounter += 1
                    j += 1
                j = 0
                i += 1
            playerMap[yAxis-1][xAxis-1] = mineCounter
            return playerMap

        if(xAxis > width-1): #In case the inserted X is on the right most point of the board
            mineCounter = i = j = 0
            for i in range(2):
                for j in range(2):
                    if(mineField[yAxis-1-i][xAxis-1-j] == "X"):
                        mineCounter += 1
                    j += 1
                j = 0
                i += 1
            playerMap[yAxis-1][xAxis-1] = mineCounter
            return playerMap
        
        mineCounter = i = j = 0
        for i in range(2):
            for j in range(3):
                if(mineField[yAxis-1-i][xAxis-j] == "X"):
                    mineCounter += 1
                j += 1
            j = 0
            i += 1
        playerMap[yAxis-1][xAxis-1] = mineCounter
        return playerMap

    if(xAxis-2 < 0): #In case the inserted X is on the left most spot of the board
        mineCounter = i = j = 0
        for i in range(3):
            for j in range(2):
                if(mineField[yAxis-i][xAxis-j] == "X"):
                    mineCounter += 1
                j += 1
            j = 0
            i += 1
        playerMap[yAxis-1][xAxis-1] = mineCounter
        return playerMap

    if(xAxis > width-1): #In case the inserted X is on the right most point of the board
        mineCounter = i = j = 0
        for i in range(3):
            for j in range(2):
                if(mineField[yAxis-i][xAxis-1-j] == "X"):
                    mineCounter += 1
                j += 1
            j = 0
            i += 1
        playerMap[yAxis-1][xAxis-1] = mineCounter
        return playerMap
    
    mineCounter = i = j = 0
    for i in range(3):
        for j in range(3):
            if(mineField[yAxis-i][xAxis-j] == "X"):
                mineCounter += 1
            j += 1
        j = 0
        i += 1
    playerMap[yAxis-1][xAxis-1] = mineCounter

    return playerMap
    
def printPlayerMap(playerMap, mineCounter):
    mapSize = len(playerMap)
    i = j = 0

    print("   ", end="")
    for i in range(mapSize):
        if(i < 9):
            print("  " + str(i+1) + " ", end="")
        else:
            print(" " + str(i+1) + " ", end="")
        i += 1
    
    print("")

    i = 0
    for i in range(mapSize):
        
        print("    ", end="")
        
        for j in range(mapSize*4-1):
            print("-", end="")
            j += 1
        print("")
        
        j = 0

        if(j < 9):
            print(" " + str(i+1) + " ", end="")
        else:
            print(str(i+1) + " ", end="")

        for j in range(mapSize):
            print("| " + str(playerMap[i][j]) + " ", end="")
            j += 1

        print("|")
        
        j = 0
        i += 1

    j = 0
    print("    ", end="")

    for j in range(mapSize*4-1):
        print("-", end="")
        j += 1
    print("")

    print("Mines left: " + str(mineCounter[0]))

def flagSpot(xAxis, yAxis, playerMap, mineCounter):
    
    playerMap[yAxis-1][xAxis-1] = "F"
    print(mineCounter)
    mineCounter[0] -= 1

    playerMap.append(mineCounter)
    return playerMap
