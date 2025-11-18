from ..core import core
from ..cli import welcome_user
from ..games.gcd_game import gcd


def main() -> None:
    name = welcome_user()
    core(gcd, name)


if __name__ == "__main__":
    main()
