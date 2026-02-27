# WRITE YOUR SOLUTION HERE:
import string


def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        words = [
            word.strip(string.punctuation)
            for word in f.read().split()
            if word.strip(string.punctuation)
        ]
    return {
        word: words.count(word)
        for word in set(words)
        if words.count(word) >= lower_limit
    }
