# WRITE YOUR SOLUTION HERE:
def filter_forbidden(word: str, forbidden: str):
    return "".join([char for char in word if char not in forbidden])
