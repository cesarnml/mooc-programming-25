# Write your solution here
layers = int(input("Layers: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = 1 + 2 * (layers - 1)

board = []

for i in range(size):
    board.append([])
    for j in range(size):
        board[i].append(0)

for i in range(layers):
    letter = alphabet[layers - 1 - i]
    row1 = i
    row2 = size - 1 - i
    col1 = row1
    col2 = row2
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0 and (i == row1 or i == row2 or j == col1 or j == col2):
                board[i][j] = letter

for i in range(size):
    for j in range(size):
        print(board[i][j], end="")
    print()
