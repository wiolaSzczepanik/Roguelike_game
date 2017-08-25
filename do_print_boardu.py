import os
os.system('clear')

with open("firstlevel.csv") as f:
    text = f.read()
    text = text.split("\n")
    board = []
    for each in text:
        board.append(list(each))
    player = "@"
    board[0][59] = player
    for row in board:
        print("".join(row))
