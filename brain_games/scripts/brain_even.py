from brain_games.games.even import parity_check
from brain_games.modules import starting_game


def main():
    text_game = 'Answer "yes" if the number is even, otherwise answer "no".'    
    starting_game(text_game, parity_check)


if __name__ == '__main__':
    main()