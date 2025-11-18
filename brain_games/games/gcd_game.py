from ..core import Response
from random import randint
import prompt  # type: ignore


def gcd() -> Response:
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    corrent_answer = str(get_gcd(number_one, number_two))
    print(f"Question: {number_one} {number_two}")
    answer = prompt.string("Your answer: ")
    return Response(corrent_answer, answer)


def get_gcd(first: int, second: int) -> int:
    if second > first:
        first, second = second, first
    while second != 0:
        first, second = second, first % second
    return first
