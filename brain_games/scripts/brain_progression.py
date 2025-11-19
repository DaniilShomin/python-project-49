from ..core import core
from ..cli import welcome_user
from ..games.progression_game import progression


def main() -> None:
    name = welcome_user()
    core(progression, name)


if __name__ == "__main__":
    main()
