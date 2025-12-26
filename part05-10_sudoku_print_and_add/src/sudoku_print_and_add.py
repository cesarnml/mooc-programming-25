# Write your solution here
def print_sudoku(sudoku: list):
    for row in sudoku[0:3]:
        for cell in row[0:3]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print(" ", end="")
        for cell in row[3:6]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print(" ", end="")
        for cell in row[6:9]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print()
    print()
    for row in sudoku[3:6]:
        for cell in row[0:3]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print(" ", end="")
        for cell in row[3:6]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print(" ", end="")
        for cell in row[6:9]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print()
    print()
    for row in sudoku[6:9]:
        for cell in row[0:3]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print(" ", end="")
        for cell in row[3:6]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print(" ", end="")
        for cell in row[6:9]:
            if cell == 0:
                print("_ ", end="")
            else:
                print(f"{cell} ", end="")
        print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


if __name__ == "__main__":
    sudoku = []
    for i in range(9):
        sudoku.append([])
    for i in range(9):
        for j in range(9):
            sudoku[i].append(0)
    print_sudoku(sudoku)
