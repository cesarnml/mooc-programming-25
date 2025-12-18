# Write your solution here
# Write your solution here
def row_correct(sudoku: list, row_no: int):
    target = sudoku[row_no]
    for i in range(9):
        if target.count(i + 1) > 1:
            return False
    return True


# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column = [row[column_no] for row in sudoku]
    for value in column:
        if value > 0 and column.count(value) > 1:
            return False
    return True


# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    elements = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            elements.append(sudoku[i][j])
    for ele in elements:
        if ele > 0 and elements.count(ele) > 1:
            return False
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        result = row_correct(sudoku, i)
        if not result:
            return result
    for i in range(9):
        result = column_correct(sudoku, i)
        if not result:
            return result
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            result = block_correct(sudoku, i, j)
            if not result:
                return result
    return True
