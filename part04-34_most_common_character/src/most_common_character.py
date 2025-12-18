# Write your solution here
def most_common_character(word):
    most_common_count = 0
    most_common_char = ""
    for char in word:
        if word.count(char) > most_common_count:
            most_common_count = word.count(char)
            most_common_char = char
    return most_common_char
