# Write your solution here


def dict_of_numbers():
    ones = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    numbers = {}

    for i in range(100):
        if i < 10:
            numbers[i] = ones[i]
        elif i < 20:
            numbers[i] = teens[i - 10]
        elif i % 10 == 0:
            numbers[i] = tens[i // 10]
        else:
            numbers[i] = tens[i // 10] + "-" + ones[i % 10]

    return numbers
