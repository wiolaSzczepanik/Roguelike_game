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
            move(import_board("firstlevel.csv"), 1, 61, 0, 5)
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

def print_board(board, skills):
    move()
    take_item(item, skills)
    fight(live, skills)


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


def main():
    intro_title_game("title_game.txt")
    game_menu()
    pick_game_mode()

    # skills = {}
    # equipment = []
    # title_screen()
    # story_screen()
    # next_screen(arg)
    #
    # create_character_screen()
    # next_screen()
    #
    # how_to_play()
    # next_screen()
    #
    # print_board(board1, skills)
    # next_screen()
    # print_board(board2, skills)
    # next_screen()
    # win()

main()
