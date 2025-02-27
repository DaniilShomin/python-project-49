from brain_games.games.gcd import gcd
from brain_games.modules import starting_game


def main():
    text_game = 'Find the greatest common divisor of given numbers.'    
    starting_game(text_game, gcd)


if __name__ == '__main__':
    main()