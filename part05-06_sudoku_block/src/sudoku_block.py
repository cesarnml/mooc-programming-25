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
