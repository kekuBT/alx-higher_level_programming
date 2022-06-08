#!/usr/bin/python3
def uniq_add(myList=[]):
    num = 0
    for value in set(myList):
        num += value
    return (num)
