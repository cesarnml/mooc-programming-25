# Write your solution here
def no_shouting(words: list[str]):
    result = []
    for word in words:
        if not word.isupper():
            result.append(word)
    return result
