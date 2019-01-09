from random import randint
from time import time

def randomDataGen():
    n=0
    max=0
    min=-1
    while n < 1000000:
        try:
            n = int(input("""\nHow many Data Points would you like to generate\n"""))
            break
        except ValueError:
            print("Please enter an integer\n")
            n = int(input("""\nHow many Data Points would you like to generate\n"""))
    while max == 0:
        try:
            max = int(input("""\nWhat is the maximum value you would like?\n"""))
            break
        except ValueError:
            print("Please enter an integer\n")
            max = int(input("""\nWhat is the maximum value you would like?\n"""))
    while min <0 :
        try:
            min = int(input("""\nWhat is the minimum value you would like?\n"""))
            break
        except ValueError:
            print("Please enter an integer\n")
            min = int(input("""\nWhat is the minimum value you would like?\n"""))
    start = time()
    list = []
    for i in range(0,n):
        list.append(randint(min,max))
    timeTaken = round((time() - start),6)
    print("Time taken to generate " + str(n) + " Data Points: " + str(timeTaken))
    return list


def importList(filename):
    file = open(filename, "r")
    list = []
    for line in file:
        list.append(int(line))
    file.close()
    return list

def importData():
    file = None
    file = input("Which file would you like to get data from?\nEg. filename.txt\n")
    list = importList(file)
    return list


def createDataSet():
    list = []
    choice = None
    while choice not in [1,2]:
        try:
            choice = int(input("""\nGenerate Random Data (1)
Import data from a .txt file (2)\n"""))
            break
        except ValueError:
            print("Please enter 1, or 2\n")
            choice = int(input("""\nGenerate Random Data (1)
Import data from a .txt file (2)\n"""))

    if choice == 1:
        list = randomDataGen()
    elif choice == 2:
        list = importData()

    return list
