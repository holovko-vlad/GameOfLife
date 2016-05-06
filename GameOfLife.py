#----------------------------------------------
# Conway's Game of Life
# More programs at UsingPython.com/programs
#----------------------------------------------
#

import random
import time
import os

#---------------------------------------------------------------------------
# new line

def initGrid(cols, rows, array):
    for i in range(rows):
        arrayRow = []
        for j in range(cols):
            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                arrayRow += [-1]
            else:
                ran = random.randint(0,3)
                if ran == 0:
                    arrayRow += [1]
                else:
                    arrayRow += [0]
        array += [arrayRow]

#---------------------------------------------------------------------------

def printGen(cols, rows, array, genNo):
    os.system("cls")

    print("Game of Life -- Generation " + str(genNo + 1))

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == -1:
                print("#", end=" ")
            elif array[i][j] == 1:
                print(".", end=" ")
            else:
                print(" ", end=" ")
        print("\n")

#---------------------------------------------------------------------------

def processNextGen(cols, rows, cur, nxt):
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            nxt[i][j] = processNeighbours(i, j, cur)

#---------------------------------