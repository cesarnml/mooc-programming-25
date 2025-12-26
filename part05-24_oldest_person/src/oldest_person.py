# Write your solution here
def oldest_person(people: list):
    name = people[0][0]
    oldest_person = people[0][1]
    for person in people:
        if person[1] < oldest_person:
            oldest_person = person[1]
            name = person[0]
    return name
