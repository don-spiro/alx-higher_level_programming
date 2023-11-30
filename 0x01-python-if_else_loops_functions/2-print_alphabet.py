#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
