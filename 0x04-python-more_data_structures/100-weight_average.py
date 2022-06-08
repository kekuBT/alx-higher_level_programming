#!/usr/bin/python3
def weight_average(myList=[]):
    if myList == [] or myList is None:
        return 0
    sums = total = 0
    for (x, y) in myList:
        sums += (x * y)
        total += y
    return sums / total
