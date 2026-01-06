# tee ratkaisu tänne
# tee ratkaisu tänne
# write your solution here

if False:
    student_data = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_data = "course1.txt"
else:
    student_data = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data = input("Course information: ")

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


def exe_to_points(exercise_points: list):

    raw_ex_points = sum(exercise_points)
    return raw_ex_points // 4


def grade(total_score):
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


def write_statistics(filename: str):
    with open(filename, "a") as file:
        file.write(
            f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"
        )
        for id, name in students.items():
            file.write(
                f"{name:30}{sum(exercises[id]):<10}{exe_to_points(exercises[id]):<10}{sum(exams[id]):<10}{exe_to_points(exercises[id]) + sum(exams[id]):<10}{grade(exe_to_points(exercises[id]) + sum(exams[id])):<10}\n"
            )


def write_header(filename: str):
    course_info = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split(": ")
            course_info.append(line[1])
    with open("results.txt", "w") as file:
        h1 = f"{course_info[0]}, {course_info[1]} credits"
        file.write(f"{h1}\n")
        file.write(f"{len(h1) * '='}\n")


write_header(course_data)
write_statistics("results.txt")

with open("results.csv", "w") as file:
    for id, name in students.items():
        file.write(
            f"{id};{name};{grade(exe_to_points(exercises[id]) + sum(exams[id]))}\n"
        )
print("Results written to files results.txt and results.csv")
