# Write your solution here
def line(num, word):
    if word == "":
        print(num * "*")
    else:
        print(num * word[0])


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
