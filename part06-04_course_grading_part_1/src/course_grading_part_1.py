# write your solution here
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

students = {}
exercises = {}

with open(student_file) as file:
    for line in file:
        row = line.split(";")
        if row[0] == "id":
            continue
        students[row[0]] = f"{row[1]} {row[2].strip()}"

with open(exercise_file) as file:
    for line in file:
        row = line.split(";")
        if row[0] == "id":
            continue
        exercises[row[0]] = []
        for ex in row[1:]:
            exercises[row[0]].append(int(ex))

for id, student in students.items():
    print(f"{student} {sum(exercises[id])}")
