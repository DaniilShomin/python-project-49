from ..configs import (
    MIN_MAX_PROGRESSION_LENGTH,
    MIN_MAX_PROGRESSION_START,
    MIN_MAX_PROGRESSION_STEP,
)
from ..core import Response
from ..utils import get_random_number


def progression() -> Response:
    start = get_random_number(*MIN_MAX_PROGRESSION_START)
    step = get_random_number(*MIN_MAX_PROGRESSION_STEP)
    lenght = get_random_number(*MIN_MAX_PROGRESSION_LENGTH)
    progression = get_progression(start, step, lenght)
    hidden_position = get_random_number(0, lenght - 1)
    correct_answer = progression[hidden_position]
    progression[hidden_position] = ".."
    question = f"Question: {' '.join(progression)}"
    return Response(question, correct_answer)


def get_progression(start: int, step: int, lenght: int) -> list[str]:
    return [str(start + step * i) for i in range(lenght)]
