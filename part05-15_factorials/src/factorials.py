# Write your solution here
def factorials(n: int):
    my_dict = {}
    for i in range(1, n + 1):
        value = 1
        for j in range(i, 0, -1):
            value *= j
        my_dict[i] = value
    return my_dict
