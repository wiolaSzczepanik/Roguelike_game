import time
import sys
import os
import datetime
import fight
from operator import itemgetter
import coldwarm

def print_title(filename):
    game_title = open(filename, "r")
    print_game_name = game_title.read()
    print(print_game_name)
    time.sleep(1.0)
    os.system('clear')
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


def creation_screen():
    name_player = input("Jak na imie ma Twój bohater: " + '\n')
    player_character = input("Wybierz dowolny znak jakim chcesz grać : " + '\n')

    while len(player_character) > 1:
        print("Wybierzy tylko jeden znak!")
        player_character = input("Wybierz dowolny znak jakim chcesz grać : " + '\n')

    return player_character


def pick_game_mode():
    print("\n")
    question = input(str("Pick number: "))
    print('\n')

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


def level(board, y, x, exit_y, exit_x, player_character):

    player = player_character
    board[y][x] = player
    print_board(board)
    move_hero(board, player, y, x, exit_y, exit_x)


def item_gather(board, y, x):
    pos = board[y][x]
    player = '\033[1;34m@\033[1;m'
    board[y][x] = player
    statistic = import_statistics("hero_stats.csv")
    old_player = "."
    board[y-1][x] = old_player

    print(player)

    if pos == "R":
        statistic_of_gather_item = {"ws": 5}
    print_board(board)
    if pos == "F":
        statistic_of_gather_item = {"defence": 2}
    import_statistics()
    print_board(board)

    for item in statistic_of_gather_item:
        if item in statistic:
            statistic[item] += statistic_of_gather_item[item]

    export_stats(statistic, "hero_stats.csv")


def print_statistics(statistics):
    stats = import_statistics(statistics)
    print("Statystyki Twojego bohatera:")
    for k, v in stats.items():
        print("{0} : {1}".format(k, v))



def move_hero(board, player, y, x, exit_y, exit_x):
    old_player = "."
    old_y = y
    old_x = x
    board[y][x] = player
    stats = import_statistics("hero_stats.csv")
    enemy_stats = import_statistics("enemy_stats.csv")
    while board[exit_y][exit_x] != player:
        key = getch()

        if key == "q":
            exit()
        if key == "i":
            print_statistics("hero_stats.csv")
            time.sleep(3)
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

        if board[y][x] != "." and board[y][x] != "R" and board[y][x] != "F" and board[y][x] != "T" and board[y][x] != player and board[y][x] != "%":
            print("Auc! Nabiles sobie guza!")
            x = old_x
            y = old_y
            continue
        elif board[y][x] == "R":
            item_gather(board, 13, 59)
        elif board[y][x] == "F":
            item_gather(board, 3, 40)
        elif board[y][x] == "T":
            fight.fight(stats, enemy_stats)
        elif board[y][x] == "%":
            coldwarm.main()


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


def import_statistics(filename=None):
    stats = {}
    if filename:
        with open(filename) as text:
            text = list(text)
            for element in text:
                element = element.strip("\n")
                element = element.split(",")

            for item in element:
                if item in stats:
                    stats[item] += 1
                else:
                    stats[item] = 1

            return stats


def export_stats(statistics, filename=None):
    if filename:
        with open(filename, "w") as save:
            stat_to_save = [(element[0]+",")*element[1] for element in statistics.items()]
            stat_to_save[-1] = stat_to_save[-1][:-1]

            for stat in stat_to_save:
                save.write(stat)


def highscore(time):
    name = input("What's your name:")
    print("Player name:" + " " * 5 + "Time:")
    # highscore = import("highscore.csv")
    highscore = {"b": 5, "s": 7, "k": 6}
    highscore[name] = time
    rank = 1
    for k, v in sorted(highscore.items(), key=itemgetter(1)):
        print(str(rank).rjust(2),k.rjust(10)+" : " + str(v).rjust(8))
        rank += 1


def main():
    stats = {"live": 100, "attack": 5, "defence": 3, "ws": 55}
    export_stats(stats, "hero_stats.csv")
    enemy_stats = {"live" : 20, "attack" : 5, "defence" : 5, "ws" : 35}
    export_stats(enemy_stats, "enemy_stats.csv")
    print_title("title_game.txt")
    game_menu()
    pick_game_mode()
    player_character = creation_screen()
    time_start = timechecker()
    level(import_board("firstlevel.csv"), 1, 61, 0, 5, player_character)
    level(import_board("secondlevel.csv"), 16, 67, 12, 20, player_character)
    time_stop = timechecker()
    player_time = time_stop - time_start
    player_time = str(player_time)
    player_time = player_time[2:7]
    print("Twoj czas to:" + player_time)
    player_time = player_time.replace(":", ".")
    player_time = float(player_time)
    highscore(player_time)
    time.sleep(3)


if __name__ == '__main__':
    main()
