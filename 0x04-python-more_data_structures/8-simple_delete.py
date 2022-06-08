#!/usr/bin/python3
def deletes(diction, key=""):
    if (key in diction):
        del diction[key]
    return (diction)
