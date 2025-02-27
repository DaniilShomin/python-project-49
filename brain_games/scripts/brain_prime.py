from brain_games.games.prime import prime
from brain_games.modules import starting_game


def main():
    text_game = ('Answer "yes" if given number is prime. '
                'Otherwise answer "no".')   
    starting_game(text_game, prime)


if __name__ == '__main__':
    main()