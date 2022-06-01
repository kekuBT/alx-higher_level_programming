#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_char = int(repr(number)[-1])
if last_char > 5:
    print(f"Last digit of {number} is {last_char} and is greater than 5")
elif last_char == 0:
    print(f"Last digit of {number} is {last_char} and is 0")
else:
    print(f"Last digit of {number} is {last_char} and is less than 6 and not 0")
