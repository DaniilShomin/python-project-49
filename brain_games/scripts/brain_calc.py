from brain_games.games.calc import calc
from brain_games.modules import starting_game


def main():
    text_game = 'What is the result of the expression?'    
    starting_game(text_game, calc)


if __name__ == '__main__':
    main()