# write your solution here
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

students = {}
with open(student_data) as file:
    for line in file:
        row = line.split(";")
        if row[0] == "id":
            continue
        students[row[0]] = f"{row[1]} {row[2].strip()}"

exercises = {}
with open(exercise_data) as file:
    for line in file:
        row = line.split(";")
        if row[0] == "id":
            continue
        exercises[row[0]] = []
        for ex in row[1:]:
            exercises[row[0]].append(int(ex))

exams = {}
with open(exam_data) as file:
    for line in file:
        row = line.split(";")
        if row[0] == "id":
            continue
        exams[row[0]] = []
        for score in row[1:]:
            exams[row[0]].append(int(score))


def calculate_grade(exercise_points: list, exam_points: list):

    raw_ex_points = sum(exercise_points)
    if raw_ex_points >= 40:
        ex_weight = 10
    elif raw_ex_points >= 36:
        ex_weight = 9
    elif raw_ex_points >= 32:
        ex_weight = 8
    elif raw_ex_points >= 28:
        ex_weight = 7
    elif raw_ex_points >= 24:
        ex_weight = 6
    elif raw_ex_points >= 20:
        ex_weight = 5
    elif raw_ex_points >= 16:
        ex_weight = 4
    elif raw_ex_points >= 12:
        ex_weight = 3
    elif raw_ex_points >= 8:
        ex_weight = 2
    elif raw_ex_points >= 4:
        ex_weight = 1
    else:
        ex_weight = 0

    total_score = ex_weight + sum(exam_points)

    if total_score >= 28:
        return 5
    elif total_score >= 24:
        return 4
    elif total_score >= 21:
        return 3
    elif total_score >= 18:
        return 2
    elif total_score >= 15:
        return 1
    else:
        return 0


for id, name in students.items():
    print(f"{name} {calculate_grade(exercises[id], exams[id])}")
