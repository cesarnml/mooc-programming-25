# Write your solution here
from datetime import datetime


def is_it_valid(pic: str):
    control_options = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    century_char = pic[6]
    control_char = pic[10]
    year = int(pic[4:6])
    month = int(pic[2:4])
    day = int(pic[0:2])

    if len(pic) != 11:
        return False
    if century_char == "+":
        year += 1800
    elif century_char == "-":
        year += 1900
    elif century_char == "A":
        year += 2000
    else:
        return False
    try:
        dob = datetime(year, month, day)
    except ValueError:
        return False
    digit9 = int(pic[0:6] + pic[7:10])
    index = digit9 % 31
    control_char_derived = control_options[index]
    is_valid = True
    if dob > datetime.now():
        is_valid = False
    if control_char != control_char_derived:
        is_valid = False
    if not century_char in "+-A":
        is_valid = False
    return is_valid
