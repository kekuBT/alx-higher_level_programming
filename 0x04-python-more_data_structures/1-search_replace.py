#!/usr/bin/python3
def search_replace(myList, search, replace):
    lists = myList.copy()
    for idx in range(len(myList)):
        if (myList[idx] == search):
            lists[idx] = replace
    return (lists)
