#!/usr/bin/python3
for num in range(0, 100):
    if num < 99:
        print('{r:02}'.format(r=num), end=', ')
    else:
        print('{}'.format(num), end="\n")
