from brain_games.modules import starting_game


def main():
    name_game = 'prime'
    text_game = ('Answer "yes" if given number is prime. '
                'Otherwise answer "no".')   
    starting_game(name_game, text_game)


if __name__ == '__main__':
    main()