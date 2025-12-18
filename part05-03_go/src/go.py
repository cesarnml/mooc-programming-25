# Write your solution here
def who_won(game_board: list):
    count1 = 0
    count2 = 0
    for row in game_board:
        for cell in row:
            if cell == 1:
                count1 += 1
            if cell == 2:
                count2 += 1
    if count1 == count2:
        return 0
    if count1 > count2:
        return 1
    else:
        return 2
