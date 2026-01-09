# Write your solution here
from random import sample


def lottery_numbers(amount: int, lower: int, upper: int):
    options = list(range(lower, upper + 1))
    return sorted(sample(options, amount))
