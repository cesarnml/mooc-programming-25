# Write your solution here
import string


def run(program: list[str]):
    if len(program) == 0:
        return []

    result = []
    execution_index = 0
    variables = {}
    locations = {}

    for i in range(len(program)):
        if ":" in program[i]:
            goto = program[i][:-1]
            locations[goto] = i

    for char in string.ascii_uppercase:
        variables[char] = 0

    expression = program[execution_index]

    while expression != "END":
        cmd = expression.split(" ")[0]
        try:
            if cmd == "MOV":
                letter = expression.split(" ")[1]
                value = expression.split(" ")[2]
                if value in string.ascii_uppercase:
                    variables[letter] = variables[value]
                else:
                    variables[letter] = int(value)
                execution_index += 1
                expression = program[execution_index]
            elif cmd == "PRINT":
                letter = expression.split(" ")[1]
                value = variables[letter] if letter in variables else int(letter)
                result.append(value)
                execution_index += 1
                expression = program[execution_index]
            elif cmd == "ADD":
                letter = expression.split(" ")[1]
                operand = expression.split(" ")[2]
                if operand in variables:
                    variables[letter] += variables[operand]
                else:
                    variables[letter] += int(operand)
                execution_index += 1
                expression = program[execution_index]
            elif cmd == "SUB":
                letter = expression.split(" ")[1]
                operand = expression.split(" ")[2]
                if operand in variables:
                    variables[letter] -= variables[operand]
                else:
                    variables[letter] -= int(operand)
                execution_index += 1
                expression = program[execution_index]
            elif cmd == "MUL":
                letter = expression.split(" ")[1]
                operand = expression.split(" ")[2]
                if operand in variables:
                    variables[letter] *= variables[operand]
                else:
                    variables[letter] *= int(operand)
                execution_index += 1
                expression = program[execution_index]
            elif cmd == "JUMP":
                goto = expression.split(" ")[1]
                execution_index = locations[goto]
                expression = program[execution_index]
            elif cmd == "IF":
                operand1 = expression.split(" ")[1]
                operator = expression.split(" ")[2]
                operand2 = expression.split(" ")[3]
                goto = expression.split(" ")[5]
                value1 = variables[operand1] if operand1 in variables else int(operand1)
                value2 = variables[operand2] if operand2 in variables else int(operand2)
                if operator == ">":
                    if value1 > value2:
                        execution_index = locations[goto]
                        expression = program[execution_index]
                    else:
                        execution_index += 1
                        expression = program[execution_index]
                elif operator == "<":
                    if value1 < value2:
                        execution_index = locations[goto]
                        expression = program[execution_index]
                    else:
                        execution_index += 1
                        expression = program[execution_index]
                elif operator == "<=":
                    if value1 <= value2:
                        execution_index = locations[goto]
                        expression = program[execution_index]
                    else:
                        execution_index += 1
                        expression = program[execution_index]

                elif operator == ">=":
                    if value1 >= value2:
                        execution_index = locations[goto]
                        expression = program[execution_index]
                    else:
                        execution_index += 1
                        expression = program[execution_index]
                elif operator == "==":
                    if value1 == value2:
                        execution_index = locations[goto]
                        expression = program[execution_index]
                    else:
                        execution_index += 1
                        expression = program[execution_index]
                elif operator == "!=":
                    if value1 != value2:
                        execution_index = locations[goto]
                        expression = program[execution_index]
                    else:
                        execution_index += 1
                        expression = program[execution_index]
            else:
                execution_index += 1
                expression = program[execution_index]
        except IndexError:
            expression = "END"
    return result
