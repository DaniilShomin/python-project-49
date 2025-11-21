from ..configs import MIN_MAX_PRIME
from ..core import Response
from ..utils import get_random_number


def prime() -> Response:
    number = get_random_number(*MIN_MAX_PRIME)
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
