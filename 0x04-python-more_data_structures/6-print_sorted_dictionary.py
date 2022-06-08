#!/usr/bin/python3
def print_sorted_dictionary(diction):
    for i in sorted(diction.keys()):
        print("{}: {}".format(i, diction[i]))
