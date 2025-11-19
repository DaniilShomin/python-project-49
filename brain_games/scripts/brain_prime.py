from ..core import core
from ..cli import welcome_user
from ..games.prime_game import prime


def main() -> None:
    name = welcome_user()
    core(prime, name)


if __name__ == "__main__":
    main()
