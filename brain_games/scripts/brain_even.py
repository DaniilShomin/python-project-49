from ..cli import welcome_user
from ..core import core
from ..games.even_game import even_game


def main():
    name = welcome_user()
    core(even_game, name)


if __name__ == "__main__":
    main()
