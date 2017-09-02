import os
import datetime
import time
os.system('clear')

def import_board(level):
    with open(level) as f:
        text = f.read()
        text = text.split("\n")
        board = []
        for each in text:
            board.append(list(each))

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == "#":
                    board[y][x] = '\033[1;30m#\033[1;m'
                if board[y][x] == "$":
                    board[y][x] = '\033[1;32m$\033[1;m'

        return board

def print_board(board):
    os.system('clear')
    for row in board:
        print("".join(row))


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def timechecker():
    return datetime.datetime.now()


def move(board, y, x, exit_y, exit_x):
    time_start = timechecker()
    player = '\033[1;34m@\033[1;m'
    board[y][x] = player
    old_player = "."
    print_board(board)
    while board[exit_y][exit_x] != player:
        move = getch()
        if move == "q":
            exit()
        if move == "w":
            y -= 1
            if board[y][x] != ".":
                print("Auc! Nabiles sobie guza!")
                y += 1
            else:
                board[y][x] = player
                board[y+1][x] = old_player
                print_board(board)
        if move == "s":
            y += 1
            if board[y][x] != ".":
                print("Auc! Nabiles sobie guza!")
                y -= 1
            else:
                board[y][x] = player
                board[y-1][x] = old_player
                print_board(board)

        if move == "a":
            x -= 1
            if board[y][x] != ".":
                print("Auc! Nabiles sobie guza!")
                x += 1
            else:
                board[y][x] = player
                board[y][x+1] = old_player
                print_board(board)

        if move == "d":
            x += 1
            if board[y][x] != ".":
                print("Auc! Nabiles sobie guza!")
                x -= 1
            else:
                board[y][x] = player
                board[y][x-1] = old_player
                print_board(board)

    print("Brawo! Przeszedles do nastepnego etapu!")
    time_stop = timechecker()
    player_time = time_stop - time_start
    player_time = str(player_time)
    print("Twoj czas to:" + player_time[:7])
    time.sleep(3)

move(import_board("firstlevel.csv"), 1, 61, 0, 5)
move(import_board("secondlevel.csv"), 16, 67, 4, 0)
