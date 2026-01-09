# Write your solution here
import string


def run(program: list[str]):
    result = []
    execution_index = 0
    variables = {}
    locations = {}
    for i in range(len(program)):
        if ":" in program[i]:
            locations[expression[:-1]] = i
    breakpoint()
    for char in string.ascii_uppercase:
        variables[char] = 0
    expression = program[execution_index]
    while expression != "END":
        cmd = expression.split(" ")[0]
        if cmd == "MOV":
            letter = expression.split(" ")[1]
            value = expression.split(" ")[2]
            if value in string.ascii_uppercase:
                variables[letter] = variables[value]
            else:
                variables[letter] = int(value)
        if cmd == "PRINT":
            letter = expression.split(" ")[1]
            result.append(variables[letter])
        if cmd == "ADD":
            letter = expression.split(" ")[1]
            operand = expression.split(" ")[2]
            if operand in variables:
                variables[letter] += variables[operand]
            else:
                variables[letter] += int(operand)
        if cmd == "SUB":
            letter = expression.split(" ")[1]
            operand = expression.split(" ")[2]
            if operand in variables:
                variables[letter] -= variables[operand]
            else:
                variables[letter] -= int(operand)
        if cmd == "MUL":
            letter = expression.split(" ")[1]
            operand = expression.split(" ")[2]
            if operand in variables:
                variables[letter] *= variables[operand]
            else:
                variables[letter] *= int(operand)
        if ":" in cmd:
            locations[cmd[:-1]] = program.index(cmd)
        if cmd == "JUMP":
            goto = expression.split(" ")[1]
            expression = program[locations[goto]]


program4 = []
program4.append("MOV N 50")
program4.append("PRINT 2")
program4.append("MOV A 3")
program4.append("begin:")
program4.append("MOV B 2")
program4.append("MOV Z 0")
program4.append("test:")
program4.append("MOV C B")
program4.append("new:")
program4.append("IF C == A JUMP error")
program4.append("IF C > A JUMP over")
program4.append("ADD C B")
program4.append("JUMP new")
program4.append("error:")
program4.append("MOV Z 1")
program4.append("JUMP over2")
program4.append("over:")
program4.append("ADD B 1")
program4.append("IF B < A JUMP test")
program4.append("over2:")
program4.append("IF Z == 1 JUMP over3")
program4.append("PRINT A")
program4.append("over3:")
program4.append("ADD A 1")
program4.append("IF A <= N JUMP begin")
result = run(program4)
