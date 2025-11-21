from ..core import Response
from ..utils import get_random_number
from ..configs import MIN_MAX_GCD


def gcd() -> Response:
    number_one = get_random_number(*MIN_MAX_GCD)
    number_two = get_random_number(*MIN_MAX_GCD)
    correct_answer = str(get_gcd(number_one, number_two))
    question = f"Question: {number_one} {number_two}"
    return Response(question, correct_answer)


def get_gcd(first: int, second: int) -> int:
    if second > first:
        first, second = second, first
    while second != 0:
        first, second = second, first % second
    return first
