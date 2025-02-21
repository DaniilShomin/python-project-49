from brain_games.modules import starting_game


def main():
    name_game = 'even'
    text_game = 'Answer "yes" if the number is even, otherwise answer "no".'    
    starting_game(name_game, text_game)


if __name__ == '__main__':
    main()