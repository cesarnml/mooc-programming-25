# Write your solution here
def same_chars(word, index1, index2):
    if index1 >= len(word) or index2 >= len(word):
        return False
    return word[index1] == word[index2]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
