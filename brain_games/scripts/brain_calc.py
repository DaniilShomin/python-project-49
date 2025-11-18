from ..core import core
from ..exceptions import CantGetRules
from ..cli import welcome_user
from ..games.calc_game import calc


def main():
    name = welcome_user()
    try:
        core(calc, name)
    except CantGetRules:
        print("[error] : Не удалось найти правила игры")
        exit(1)


if __name__ == "__main__":
    main()
