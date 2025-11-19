from random import randint
from ..core import Response


def progression() -> Response:
    start = randint(1, 10)
    step = randint(1, 9)
    lenght = randint(5, 10)
    progression = get_progression(start, step, lenght)
    hidden_position = randint(0, lenght - 1)
    correct_answer = progression[hidden_position]
    progression[hidden_position] = ".."
    question = f"Question: {' '.join(progression)}"
    return Response(question, correct_answer)


def get_progression(start: int, step: int, lenght: int) -> list[str]:
    return [str(start + step * i) for i in range(lenght)]
