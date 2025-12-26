# Write your solution here
def create_tuple(x: int, y: int, z: int):
    smallest = min([x, y, z])
    largest = max([x, y, z])
    total = sum([x, y, z])
    return (smallest, largest, total)
