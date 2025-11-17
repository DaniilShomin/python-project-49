from ..cli import welcome_user
from ..core import core
from ..games.even_game import even_game
from ..rules import RULES


def main():
    name = welcome_user()
    rules = RULES["even"]
    core(even_game, rules, name)


if __name__ == "__main__":
    main()
