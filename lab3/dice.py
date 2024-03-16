"""dice.py"""


import random


def roll(value: int) -> None:
    if value == 1:
        print(value, "Natural Miss")
    elif 2 <= value <= 10:
        print(value, "Failure")
    elif 11 <= value <= 19:
        print(value, "Success")
    elif value == 20:
        print(value, "Critical Success!")


if __name__ == '__main__':
    roll(1)
    roll(10)
    roll(17)
    roll(20)