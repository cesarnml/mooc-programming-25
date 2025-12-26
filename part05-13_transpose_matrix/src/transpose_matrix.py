# Write your solution here
def transpose(matrix: list):
    matrix_copy = [row[:] for row in matrix]
    for i in range(len(matrix)):
        matrix[i] = []
        for j in range(len(matrix)):
            matrix[i].append(matrix_copy[j][i])
