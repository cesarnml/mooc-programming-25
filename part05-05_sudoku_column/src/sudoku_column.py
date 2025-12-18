# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column = [row[column_no] for row in sudoku]
    for value in column:
        if value > 0 and column.count(value) > 1:
            return False
    return True
