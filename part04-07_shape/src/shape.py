# Copy here code of line function from previous exercise and use it in your solution
def line(num, word):
    if word == "":
        print(num * "*")
    else:
        print(num * word[0])


def shape(size, char1, height, char2):
    for i in range(size):
        line(i + 1, char1)
    for _ in range(height):
        line(size, char2)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
