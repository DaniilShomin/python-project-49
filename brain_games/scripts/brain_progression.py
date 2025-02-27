from brain_games.games.progression import progression
from brain_games.modules import starting_game


def main():
    text_game = 'What number is missing in the progression?'    
    starting_game(text_game, progression)


if __name__ == '__main__':
    main()