# Write your solution here
from random import sample
from string import ascii_lowercase, digits


def generate_strong_password(length: int, digit: bool, special: bool):
    special_chars = "!?=+-()#"
    options = ascii_lowercase
    passwd = ""
    if digit:
        options += digits
    if special:
        options += special_chars
    while not check_password(passwd, digit, special):
        passwd = "".join(sample(options, length))
    return passwd


def check_password(password: str, digit: bool, special: bool):
    special_chars = "!?=+-()#"
    meetsDigit = not digit
    meetsSpecial = not special
    hasAlphabet = False

    if digit:
        for char in digits:
            if char in password:
                meetsDigit = True
    if special:
        for char in special_chars:
            if char in password:
                meetsSpecial = True
    for char in ascii_lowercase:
        if char in password:
            hasAlphabet = True

    return hasAlphabet and meetsDigit and meetsSpecial
