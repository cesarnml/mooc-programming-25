# Write your solution here
def row_correct(sudoku: list, row_no: int):
    target = sudoku[row_no]
    for i in range(9):
        if target.count(i + 1) > 1:
            return False
    return True
