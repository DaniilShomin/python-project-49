from ..core import core
from ..cli import welcome_user
from ..games.calc_game import calc


def main():
    name = welcome_user()
    core(calc, name)


if __name__ == "__main__":
    main()
