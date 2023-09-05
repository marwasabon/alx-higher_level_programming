#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
print("Last digit of {} is ".format(number), end="")

if number < 0:
    last = number % -10
else:
    last = number % 10

if last > 5:
    print("{} and is greater than 5".format(last))
elif last == 0:
    print("{} and is 0".format(last))
else:
    print("{} and is less than 6 and not 0".format(last))
