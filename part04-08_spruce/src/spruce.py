# Write your solution here
def spruce(size):
    print("a spruce!")
    print(" " * (size - 1) + "*")
    draw = "*"
    for i in range(size - 1):
        draw += "**"
        print(" " * (size - 2 - i) + draw)
    print(" " * (size - 1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
