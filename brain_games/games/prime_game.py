from random import randint
from ..core import Response


def prime() -> Response:
    number = randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    question = f"Question: {number}"
    return Response(question, correct_answer)


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True
