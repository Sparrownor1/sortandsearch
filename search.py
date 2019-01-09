from time import time

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def addNode(self, newValue):
        if newValue < self.value:
            if self.left != None:
                self.left.addNode(newValue)
            else:
                self.left = Node(newValue)
        elif newValue > self.value:
            if self.right != None:
                self.right.addNode(newValue)
            else:
                self.right = Node(newValue)
        # else:
            # print("Reoccurence of " + str(newValue))

    # def search(self, value):
    #     if value == self.value:
    #         print(str(value) + " is in the list")
    #         return True
    #     elif value < self.value:
    #         if self.left != None:
    #             self.left.search(value)
    #         else:
    #             print("Value not in list")
    #     elif value > self.value:
    #         if self.right != None:
    #             self.right.search(value)
    #         else:
    #             print("Value not in list")

    #How to include steps if recursively defined?
    def search(self, value):
        if value == self.value:
            print(str(value) + " is in the list")
            return True
        elif value < self.value:
            if self.left != None:
                return self.left.search(value)
            else:
                print("Value not in list")
                return False
        elif value > self.value:
            if self.right != None:
                return self.right.search(value)
            else:
                print(str(value) + " not in list")
                return False

def binaryTreeSearch(item, list):
    itemFound = False
    treeStart = time()
    node = Node(list[0])
    for i in list[1:]:
        node.addNode(i)
    treeTime = round((time() - treeStart), 6)
    print("Time taken to make tree: " + str(treeTime))
    start = time()
    itemFound = node.search(item)
    timeTaken = round((time() - start),6)
    print("Time taken to Binary Tree Search: " + str(timeTaken))
    print("""Complexity:
Big O: n
Omega: log(n)""")
    return itemFound

def linearSearch(item, list):
    itemFound = False
    steps = 0
    start = time()
    for obj in list:
        steps += 1
        if obj == item:
            print(str(item) + " is in the list")
            itemFound = True
            break
    if itemFound == False:
        print(str(item) + " is not in the list")
    timeTaken = round((time() - start),6)
    print(str(steps) + ' steps taken to Linear Search')
    print("Time taken to Linear Search: " + str(timeTaken))
    print("""Complexity:
Big O: n
Omega: 1""")
    return itemFound

def binarySearch(item, list):
    steps = 0
    first = 0
    last = len(list)-1
    itemFound = False
    start = time()
    while first<=last and not itemFound:
        steps += 1
        midpoint = (first+last)//2
        if item == list[midpoint]:
            itemFound = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    if itemFound == True:
        print(str(item) + " is in the list")
    else:
        print(str(item) + " is not in the list")
    timeTaken = round((time() - start),6)
    print(str(steps) + ' steps taken to Binary Search')
    print("Time taken to Binary Search: " + str(timeTaken))
    print("""Complexity:
Big O: log(n)
Omega: 1""")
    return itemFound

def search(list):
    choice = None
    while choice not in [1,2,3]:
        try:
            choice = int(input("""\nLinear Search (1)
Binary Search (2)
Binary Tree Search (3)\n"""))
            break
        except ValueError:
            print("Please enter 1, 2, or 3\n")
            choice = int(input("""\nLinear Search (1)
Binary Search (2)
Binary Tree Search (3)\n"""))
    itemToBeFound = None
    while 1:
        try:
            itemToBeFound = int(input("What number would you like to search for?\n"))
            break
        except ValueError:
            print("Please enter an integer\n")
            itemToBeFound = int(input("What number would you like to search for?\n"))

    if choice == 1:
        linearSearch(itemToBeFound, list)
    elif choice == 2:
        binarySearch(itemToBeFound, list)
    elif choice == 3:
        binaryTreeSearch(itemToBeFound, list)
