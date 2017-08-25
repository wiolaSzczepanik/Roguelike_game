def main():
    skills = {}
    equipment = []
    title_screen()
    story_screen()
    next_screen(arg)

    create_character_screen()
    next_screen()

    how_to_play()
    next_screen()

    print_board(board1, skills)
    next_screen()
    print_board(board2, skills)
    next_screen()
    win()


def print_board(board, skills):
    move()
    take_item(item, skills)
    fight(live, skills)
