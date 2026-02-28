# Write your solution here


def prime_numbers():
    def is_prime(number):
        for test_num in range(2, number):
            if number % test_num == 0:
                return False
        return True

    current = 2
    while True:
        if is_prime(current):
            yield current
        current += 1
