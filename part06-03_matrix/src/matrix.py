# write your solution here
def matrix_sum():
    total = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            row = [int(x) for x in line.split(",")]
            total += sum(row)
    return total


def matrix_max():
    max = float("-inf")
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            for number in line.split(","):
                if int(number) > max:
                    max = int(number)
    return max


def row_sums():
    sums = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            numbers = [int(x) for x in line.split(",")]
            sums.append(sum(numbers))
    return sums
