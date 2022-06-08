#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

myList = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(myList)
print("Average: {:0.2f}".format(result))
