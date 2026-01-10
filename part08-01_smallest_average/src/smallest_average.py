# Write your solution here


def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest_average = float("inf")
    result = {}
    for person in [person1, person2, person3]:
        current_average = 0
        count = 0
        for value in person.values():
            if type(value) == int:
                current_average += value
                count += 1
        if current_average / count < smallest_average:
            smallest_average = current_average / count
            result = person
    return result
