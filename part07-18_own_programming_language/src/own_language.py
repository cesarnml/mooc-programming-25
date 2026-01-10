# Write your solution here
import string


def getValue(letterOrInt: str, variables: dict[str, int]) -> int:
    return variables[letterOrInt] if letterOrInt in variables else int(letterOrInt)


def evaluate(operand1: str, operator: str, operand2: str, variables: dict[str, int]):
    value1 = getValue(operand1, variables)
    value2 = getValue(operand2, variables)
    if operator == ">":
        return value1 > value2
    elif operator == "<":
        return value1 < value2
    elif operator == "<=":
        return value1 <= value2
    elif operator == ">=":
        return value1 >= value2
    elif operator == "==":
        return value1 == value2
    elif operator == "!=":
        return value1 != value2
    else:
        raise ValueError(f"Invalid operator: {operator}")


def run(program: list[str]):
    execution_index = 0
    variables = {}
    locations = {}
    result = []

    for i in range(len(program)):
        if ":" in program[i]:
            goto = program[i][:-1]
            locations[goto] = i

    for char in string.ascii_uppercase:
        variables[char] = 0

    while execution_index < len(program):
        expression = program[execution_index]
        if expression == "END":
            break

        parts = expression.split(" ")
        cmd = parts[0]

        if cmd == "MOV":
            variables[parts[1]] = getValue(parts[2], variables)
            execution_index += 1
        elif cmd == "PRINT":
            result.append(getValue(parts[1], variables))
            execution_index += 1
        elif cmd == "ADD":
            variables[parts[1]] += getValue(parts[2], variables)
            execution_index += 1
        elif cmd == "SUB":
            variables[parts[1]] -= getValue(parts[2], variables)
            execution_index += 1
        elif cmd == "MUL":
            variables[parts[1]] *= getValue(parts[2], variables)
            execution_index += 1
        elif cmd == "JUMP":
            execution_index = locations[parts[1]]
        elif cmd == "IF":
            if evaluate(parts[1], parts[2], parts[3], variables):
                execution_index = locations[parts[5]]
            else:
                execution_index += 1
        else:
            # Label or unknown command - just skip
            execution_index += 1

    return result
