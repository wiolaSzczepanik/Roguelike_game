import time
import sys


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
            print("1")
            print("\n")
            break
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
