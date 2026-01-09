# Write your solution here
from string import ascii_letters, punctuation


def separate_characters(my_string: str):
    asci = ""
    punc = ""
    others = ""
    for char in my_string:
        if char in ascii_letters:
            asci += char
        elif char in punctuation:
            punc += char
        else:
            others += char
    return asci, punc, others
