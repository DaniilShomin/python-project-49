from ..core import Response
from random import randint
import prompt  # type: ignore



def prime() -> Response:
    number = randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    return Response(correct_answer, answer)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
        
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


