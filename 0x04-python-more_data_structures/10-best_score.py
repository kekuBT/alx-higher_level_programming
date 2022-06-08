#!/usr/bin/python3
def best_score(diction):
    if (diction == {} or diction is None):
        return (None)
    else:
        max_value = max(diction, key=diction.get)
        return (max_value)
