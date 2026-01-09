# Write your solution here
def new_person(name: str, age: int):
    if name == "" or len(name.split(" ")) < 2 or len(name) > 40:
        raise ValueError("name must be at least two words and less than 40 characters")
    if age > 150 or age < 0:
        raise ValueError("number must be positive and less than 150")
    return name, age
