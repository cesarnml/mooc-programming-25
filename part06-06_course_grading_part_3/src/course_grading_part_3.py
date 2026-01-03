# tee ratkaisu tänne
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


print(
    f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
)
for id, name in students.items():
    print(
        f"{name:30}{sum(exercises[id]):<10}{exe_to_points(exercises[id]):<10}{sum(exams[id]):<10}{exe_to_points(exercises[id]) + sum(exams[id]):<10}{grade(exe_to_points(exercises[id]) + sum(exams[id])):<10}"
    )
