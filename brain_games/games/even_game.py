from random import randint
from ..core import Response
import prompt  # type: ignore


def even_game() -> Response:
    question = randint(1, 100)
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    correct_answer = "yes" if is_even(question) else "no"
    return Response(correct_answer, answer)


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False
