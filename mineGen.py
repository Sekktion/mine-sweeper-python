import random

def generateMinefield(playMap):
    
    width = len(playMap[0])
    height = len(playMap)

    totalSize = width*height

    totalMines = int((float(totalSize)*25)/100)
    
    mineQuantity = 0

    i = j = counter = 0

    for i in range(0,height):
        for j in range(0,width):
            seed = random.randint(1,100)
            chance = (totalMines-mineQuantity)/(totalSize-counter)*100
            if(seed <= chance and totalMines > mineQuantity):
                playMap[i][j] = "X"
                mineQuantity += 1
            counter += 1
    
    return playMap