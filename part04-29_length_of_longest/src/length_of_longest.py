# Write your solution here
def length_of_longest(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest
