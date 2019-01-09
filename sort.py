from time import time

def bubbleSort(list):
    steps = 0
    swapCount = -1
    first = 0
    last = len(list)-1
    start = time()
    while swapCount != 0:
        swapCount = 0
        for i in range(0,last):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i]=list[i+1]
                list[i+1]=temp
                swapCount += 1
                steps += 1
    timeTaken = round((time() - start),6)
    print(str(steps) + ' steps taken to bubble sort')
    print("Time taken to Bubble Sort: " + str(timeTaken))
    print("""Complexity:
Big O: n
Omega: n*n""")

def mergeSort(list):
    steps = 0
    start = time()
    mergeSort2(list, 0, len(list)-1)
    timeTaken = round((time() - start),6)
    print("Time taken to Merge Sort: " + str(timeTaken))
    print("""Complexity:
Big O: n log(n)
Omega: n log(n)""")
    # print(str(steps) + ' steps taken to bubble sort')


def mergeSort2(list, first, last):
    if first < last:
        middle = (first+last)//2
        mergeSort2(list, first, middle)
        mergeSort2(list, middle+1, last)
        merge(list, first, middle, last)

def merge(list,first,middle,last):
    L = list[first:middle+1]
    R = list[middle+1:last+1]
    L.append(9999999999999)
    R.append(9999999999999)
    l = r = 0
    for k in range(first, last+1):
        if L[l] <= R[r]:
            list[k] = L[l]
            l += 1
        else:
            list[k] = R[r]
            r += 1

def sort(list):
    choice = None
    while choice not in [1,2]:
        try:
            choice = int(input("""\nMerge Sort (1)
Bubble Sort (2)\n"""))
            break
        except ValueError:
            print("Please enter 1, 2, or 3\n")
            choice = int(input("""\nLinear Search (1)
Binary Search (2)
Binary Tree Search (3)\n"""))

    if choice == 1:
        mergeSort(list)
    elif choice == 2:
        bubbleSort(list)
