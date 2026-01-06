# Write your solution here
def evaluate(problem: str):
    if "-" in problem:
        operand1, operand2 = problem.split("-")
        return int(operand1) - int(operand2)
    operand1, operand2 = problem.split("+")
    return int(operand1) + int(operand2)


def filter_solutions():
    with open("solutions.csv", "r") as file:
        open("correct.csv", "w").close()
        open("incorrect.csv", "w").close()
        for line in file:
            name, problem, result = line.strip().split(";")
            if evaluate(problem) == int(result):
                with open("correct.csv", "a") as output:
                    output.write(f"{name};{problem};{result}\n")
            else:
                with open("incorrect.csv", "a") as output:
                    output.write(f"{name};{problem};{result}\n")
