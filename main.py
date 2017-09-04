def intro_title_game(filename):
    game_title = open(filename, "r")
    print_game_name = game_title.read()
    print(print_game_name)
    game_title.close()


def print_board(board, skills):
    move()
    take_item(item, skills)
    fight(live, skills)


def main():
    intro_title_game()
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
