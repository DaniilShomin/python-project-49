from ..core import Response
from random import randint
import prompt  # type: ignore


def progression() -> Response:
    start = randint(1, 10)
    step = randint(1, 9)
    lenght = randint(5, 10)
    progression = get_progression(start, step, lenght)
    hidden_position = randint(0, lenght - 1)
    correct_answer = progression[hidden_position]
    progression[hidden_position] = ".."
    print(f"Question: {' '.join(progression)}")
    answer = prompt.string("Your aswer: ")
    return Response(correct_answer, answer)


def get_progression(start: int, step: int, lenght: int) -> list[str]:
    return [str(start + step * i) for i in range(lenght)]
