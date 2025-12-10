# Write your solution here
def greatest_number(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
