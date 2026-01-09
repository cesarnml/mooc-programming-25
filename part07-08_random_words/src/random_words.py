# Write your solution here
from random import sample


def words(n: int, beginning: str):
    dictionary: list[str] = []
    with open("words.txt", "r") as file:
        for line in file:
            dictionary.append(line.strip())
    options = []
    for word in dictionary:
        if word.startswith(beginning):
            options.append(word)
    if len(options) < n:
        raise ValueError("Insufficient number of words available")
    return sample(options, n)
