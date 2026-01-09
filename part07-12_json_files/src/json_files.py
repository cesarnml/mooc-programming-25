# Write your solution here
import json


def print_persons(filename: str):
    with open(filename, "r") as file:
        data = file.read()
    persons = json.loads(data)
    for person in persons:
        print(
            f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})"
        )
