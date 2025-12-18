# Write your solution here
def longest(words: list):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
