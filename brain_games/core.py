from typing import Callable, NamedTuple
from .configs import MAX_GAME_COUNT, RULES
import __main__
from .exceptions import CantGetRules
import prompt  # type: ignore


class Response(NamedTuple):
    question: str
    correct_answer: str


def core(game: Callable[[], Response]) -> None:
    name_user = welcome_user()
    try:
        rule = get_rules()
    except CantGetRules:
        print("[error] : Не удалось найти правила игры")
        exit(1)
    print(rule)

    count_game = 0
    while count_game < MAX_GAME_COUNT:
        round = game()
        print(round.question)
        answer = prompt.string("Your answer: ")
        if not is_win(round.correct_answer, answer):
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{round.correct_answer}'."
            )
            print(f"Let's try again, {name_user}!")
            break
        print("Correct")
        count_game += 1
    else:
        print(f"Congratulations, {name_user}!")


def is_win(result_game: str, user_answer: str) -> bool:
    if result_game == user_answer:
        return True
    return False


def get_rules() -> str:
    name_game = __main__.__file__.split("/")[-1]
    try:
        rules = RULES[name_game]
        return rules
    except KeyError:
        raise CantGetRules


def welcome_user() -> str:
    print("Welcome to the Brain Game!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name
