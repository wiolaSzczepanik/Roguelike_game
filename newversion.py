import time
import sys
import os
import datetime
import fight


def intro_title_game(filename):
    game_title = open(filename, "r")
    print_game_name = game_title.read()
    print(print_game_name)
    game_title.close()


def intro_story_about_game(filename):
    intro_story_about_game = []
    with open(filename) as file:
        for line in file:
            split_line = line.strip().split(",")
            for i in range(0, len(split_line)):
                split_line[i] = split_line[i].strip()
            intro_story_about_game.append(split_line)

    for i in range(len(intro_story_about_game)):  # module for slow printings
        line = " . " * 2 + " ".join(intro_story_about_game[i])
        for l in line:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.025)
        print ('')

def how_to_play(filename):
    how_to_play_text = []
    with open(filename) as file:
        for line in file:
            split_line = line.strip().split(",")
            for i in range(0, len(split_line)):
                split_line[i] = split_line[i].strip()
            how_to_play_text.append(split_line)

    for i in range(len(how_to_play_text)):  # module for slow printings
        line = " . " * 2 + " ".join(how_to_play_text[i])
        for l in line:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.025)
        print ('')


def game_menu():
    print("MENU:", "\n")
    print("1--->START GAME")
    print("2--->GAME STORY")
    print("3--->HOW TO PLAY")
    print("4--->END GAME")


def pick_game_mode():
    question = input(str("Pick number: "))

    while question != range(1, 4):
        if question == "1":
            return True
        elif question == "2":
            intro_story_about_game("story.txt")
            game_menu()
            pick_game_mode()
            print("\n")
            break
        elif question == "3":
            how_to_play("how_to_play.txt")
            game_menu()
            pick_game_mode()
            print("\n")
            break
        elif question == "4":
            print("See you next time")
            print("\n")
            break
        else:
            print("You pick wrong number. Try again")


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


def level(board, y, x):
    player = "@"
    board[y][x] = player
    print_board(board)
    move_hero(board, player, y, x)


def move_hero(board, player, y, x):
    old_player = "."
    old_y = y
    old_x = x
    board[y][x] = player

    while True:
        key = getch()

        if key == "q":
            exit()
        if key == "i":
            pass

        if key == "w":
            y -= 1
            old_y = y + 1
            old_x = x
        elif key == "s":
            y += 1
            old_y = y - 1
            old_x = x
        elif key == "a":
            x -= 1
            old_x = x + 1
            old_y = y
        elif key == "d":
            x += 1
            old_x = x - 1
            old_y = y

        if board[y][x] != "." and board[y][x] != "R" and board[y][x] != "F" and board[y][x] != "T":
            print("Auc! Nabiles sobie guza!")
            x = old_x
            y = old_y
            continue
        # elif board[y][x] == "F":

        board[y][x] = player
        board[old_y][old_x] = old_player
        print_board(board)






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


def main():
    intro_title_game("title_game.txt")
    game_menu()
    pick_game_mode()
    level(import_board("firstlevel.csv"), 1, 61)

main()
