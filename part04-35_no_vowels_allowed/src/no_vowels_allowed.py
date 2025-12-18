# Write your solution here
def no_vowels(word):
    result = ""
    for char in word:
        if not char in "aeiou":
            result += char
    return result
