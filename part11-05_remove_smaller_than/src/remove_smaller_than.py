# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(numbers: list[int], limit: int):
    return [number for number in numbers if number >= limit]
