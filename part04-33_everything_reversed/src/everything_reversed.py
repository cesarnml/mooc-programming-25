# Write your solution here
def everything_reversed(words: list):
    result = []
    for word in words:
        result.append(word[::-1])
    return result[::-1]
