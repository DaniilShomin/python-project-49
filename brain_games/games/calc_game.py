from random import randint, choice
from operator import sub, mul, add
import prompt  # type: ignore
from ..core import Response


calc_sign = {
    sub: "-",
    mul: "*",
    add: "+",
}


def calc():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    random_calc_sign = choice(list(calc_sign))
    correct_answer = str(random_calc_sign(number_one, number_two))
    print(f"Question: {number_one} {calc_sign[random_calc_sign]} {number_two}")
    answer = prompt.string("Your answer: ")
    return Response(correct_answer, answer)
