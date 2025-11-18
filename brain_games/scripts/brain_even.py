from ..cli import welcome_user
from ..core import core
from ..games.even_game import even_game
from ..exceptions import CantGetRules


def main():
    name = welcome_user()
    try:
        core(even_game, name)
    except CantGetRules:
        print("[error] : Не удалось найти правила игры")
        exit(1)


if __name__ == "__main__":
    main()
