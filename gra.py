import os
import datetime
import time
import fight
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

def print_board(board, live, statistic):
    os.system('clear')
    for row in board:
        print("".join(row))
    print("HP: " + str(live))
    for skill in statistic:
        print(skill, statistic[skill], "   ", end="")
    print("")

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
    live = 100 # dorobic import
    statistic = {"atak" :10, "obrona": 3, "wiedza": 5, "ww" : 55} # dorobic import
    enemy = {"atak" :3, "obrona": 3, "wiedza": 5, "ww" : 35} # import?
    time_start = timechecker() # przeniesc do maina
    player = '\033[1;34m@\033[1;m'
    board[y][x] = player
    old_player = "."
    print_board(board, live, statistic)
    while board[exit_y][exit_x] != player:
        move = getch()
        if move == "q":
            exit()
        if move == "w":
            y -= 1
            if board[y][x] != "." and board[y][x] != "T":
                print("Auc! Nabiles sobie guza!")
                y += 1
            elif board[y][x] == "T":
                fight.fight(live, statistic, 20, enemy)
                board[y][x] = player
                board[y+1][x] = old_player
                print_board(board, live, statistic)
            else:
                board[y][x] = player
                board[y+1][x] = old_player
                print_board(board, live, statistic)
        if move == "s":
            y += 1
            if board[y][x] != "." and board[y][x] != "T":
                print("Auc! Nabiles sobie guza!")
                y -= 1
            elif board[y][x] == "T":
                fight.fight(live, statistic, 20, enemy)
                board[y][x] = player
                board[y-1][x] = old_player
                print_board(board, live, statistic)
            else:
                board[y][x] = player
                board[y-1][x] = old_player
                print_board(board, live, statistic)

        if move == "a":
            x -= 1
            if board[y][x] != "." and board[y][x] != "T":
                print("Auc! Nabiles sobie guza!")
                x += 1
            elif board[y][x] == "T":
                fight.fight(live, statistic, 20, enemy)
                board[y][x] = player
                board[y][x+1] = old_player
                print_board(board, live, statistic)
            else:
                board[y][x] = player
                board[y][x+1] = old_player
                print_board(board, live, statistic)

        if move == "d":
            x += 1
            if board[y][x] != "." and board[y][x] != "T":
                print("Auc! Nabiles sobie guza!")
                x -= 1
            elif board[y][x] == "T":
                fight.fight(live, statistic, 20, enemy)
                board[y][x] = player
                board[y][x-1] = old_player
                print_board(board, live, statistic, inventory)
            else:
                board[y][x] = player
                board[y][x-1] = old_player
                print_board(board, live, statistic)

    print("Brawo! Przeszedles do nastepnego etapu!")
    time_stop = timechecker()
    player_time = time_stop - time_start
    player_time = str(player_time)
    print("Twoj czas to:" + player_time[:7])
    time.sleep(3)



move(import_board("firstlevel.csv"), 1, 61, 0, 5)
move(import_board("secondlevel.csv"), 16, 67, 4, 0)
