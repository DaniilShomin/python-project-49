from ..core import Response
from random import randint


def gcd() -> Response:
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    correct_answer = str(get_gcd(number_one, number_two))
    question = f"Question: {number_one} {number_two}"
    return Response(question, correct_answer)


def get_gcd(first: int, second: int) -> int:
    if second > first:
        first, second = second, first
    while second != 0:
        first, second = second, first % second
    return first
