# Write your solution here
import string


def change_case(orig_string: str):
    output = ""
    for char in orig_string:
        if char in string.ascii_lowercase:
            output += char.upper()
        elif char in string.ascii_uppercase:
            output += char.lower()
        else:
            output += char
    return output


def split_in_half(orig_string: str):
    first_half = len(orig_string) // 2
    return orig_string[:first_half], orig_string[first_half:]


def remove_special_characters(orig_string: str):
    result = ""
    options = string.ascii_letters + string.whitespace + string.digits
    for char in orig_string:
        if char in options:
            result += char
    return result
