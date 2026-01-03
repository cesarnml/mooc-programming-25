# write your solution here
def largest():
    max = float("-inf")
    with open("numbers.txt") as file:
        for number in file:
            integer = int(number)
            if integer > max:
                max = integer
    return max
