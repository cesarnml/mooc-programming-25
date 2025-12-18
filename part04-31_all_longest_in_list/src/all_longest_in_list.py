# Write your solution here
def all_the_longest(words):
    longest = 0
    all_longest = []
    for word in words:
        if len(word) > longest:
            longest = len(word)
    for word in words:
        if len(word) == longest:
            all_longest.append(word)
    return all_longest
