#!/usr/bin/python3
def complex_delete(diction, value):
    for key in list(diction.keys()):
        if diction[key] == value:
            diction.pop(key, None)
    return diction
