from ..core import Response
from ..utils import get_random_number
from ..configs import MIN_MAX_EVEN


def even_game() -> Response:
    number = get_random_number(*MIN_MAX_EVEN)
    question = f"Question: {number}"
    correct_answer = "yes" if is_even(number) else "no"
    return Response(question, correct_answer)


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False
