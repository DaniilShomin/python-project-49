from operator import add, mul, sub
from random import choice

from ..configs import MIN_MAX_CALC
from ..core import Response
from ..utils import get_random_number

calc_sign = {
    sub: "-",
    mul: "*",
    add: "+",
}


def calc() -> Response:
    number_one = get_random_number(*MIN_MAX_CALC)
    number_two = get_random_number(*MIN_MAX_CALC)
    random_calc_sign = choice(list(calc_sign))
    correct_answer = str(random_calc_sign(number_one, number_two))
    sign = calc_sign[random_calc_sign]
    question = f"Question: {number_one} {sign} {number_two}"
    return Response(question, correct_answer)
