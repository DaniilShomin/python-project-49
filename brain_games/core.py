from typing import Callable, NamedTuple
from .configs import MAX_GAME_COUNT, RULES
import __main__


class Response(NamedTuple):
    correct: str
    user: str


def core(game: Callable, name_user: str) -> None:
    count_game = 0
    print(get_rules())
    while count_game < MAX_GAME_COUNT:
        result = game()
        if not is_win(result):
            print(f"'{result.user}' is wrong answer ;(. Correct answer was '{result.correct}'.")
            break
        print("Correct")
        count_game += 1
    if count_game != MAX_GAME_COUNT:
        print(f"Let's try again, {name_user}")
    else:
        print(f"Congratulations, {name_user}")


def is_win(response: Response) -> bool:
    if response.correct == response.user:
        return True
    return False


def get_rules() -> str:
    name_game = __main__.__file__.split("/")[-1]
    return RULES[name_game]
