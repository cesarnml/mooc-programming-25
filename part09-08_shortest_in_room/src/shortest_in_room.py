# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons: list[Person] = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        total_height = sum(person.height for person in self.persons)
        print(
            f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm"
        )
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.persons) == 0:
            return None
        shortest = self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        shortest = self.shortest()
        self.persons.remove(shortest)
        return shortest


if __name__ == "__main__":
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Ally", 166))
    # room.add(Person("Nina", 162))
    # room.add(Person("Dorothy", 155))
    # print("Is the room empty?", room.is_empty())
    # room.print_contents()
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()
