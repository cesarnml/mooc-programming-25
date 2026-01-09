# Write your solution here
from random import choice


def roll(die: str):
    dieA = [3, 3, 3, 3, 3, 6]
    dieB = [2, 2, 2, 5, 5, 5]
    dieC = [1, 4, 4, 4, 4, 4]
    if die == "A":
        return choice(dieA)
    if die == "B":
        return choice(dieB)
    if die == "C":
        return choice(dieC)


def play(die1: str, die2: str, times: int):
    win1 = 0
    win2 = 0
    tie = 0
    for i in range(times):
        outcome1 = roll(die1)
        outcome2 = roll(die2)
        if outcome1 > outcome2:
            win1 += 1
        elif outcome2 > outcome1:
            win2 += 1
        else:
            tie += 1
    return win1, win2, tie
