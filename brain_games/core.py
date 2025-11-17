from typing import Callable, NamedTuple


MAX_GAME_COUNT = 3


class Response(NamedTuple):
    correct: str
    user: str


def core(game: Callable, rules: str, name_user: str) -> None:
    count_game = 0
    print(rules)
    while count_game < MAX_GAME_COUNT:
        result = game()
        if is_win(result):
            print("Correct")
        else:
            print(f"'{result.user}' is wrong answer ;(. Correct answer was '{result.correct}'.")
            break
        count_game += 1
    if count_game != MAX_GAME_COUNT:
        print(f"Let's try again, {name_user}")
    else:
        print(f"Congratulations, {name_user}")


def is_win(response: Response) -> bool:
    if response.correct == response.user:
        return True
    return False
