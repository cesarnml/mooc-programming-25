# Write your solution here
from random import choice
from string import ascii_lowercase


def generate_password(length: int):
    output = ""
    for _ in list(range(length)):
        output += choice(ascii_lowercase)
    return output
