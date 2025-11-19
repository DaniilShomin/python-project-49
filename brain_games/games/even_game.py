from random import randint
from ..core import Response


def even_game() -> Response:
    number = randint(1, 100)
    question = f"Question: {number}"
    correct_answer = "yes" if is_even(number) else "no"
    return Response(question, correct_answer)


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False
