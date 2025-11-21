MAX_GAME_COUNT = 3

RULES = {
    "brain-even": 'Answer "yes" if the number is even, otherwise answer "no".',
    "brain-calc": "What is the result of the expresion?",
    "brain-gcd": "Find the greatest common divisor of given numbers.",
    "brain-progression": "What number is missing in the progression?",
    "brain-prime": """Answer "yes" if given number is prime. 
                    Otherwise answer "no".""",
}

# min max values for gas
MIN_MAX_CALC = (1, 100)
MIN_MAX_EVEN = (1, 100)
MIN_MAX_GCD = (1, 100)
MIN_MAX_PRIME = (1, 100)

MIN_MAX_PROGRESSION_START = (1, 10)
MIN_MAX_PROGRESSION_STEP = (1, 10)
MIN_MAX_PROGRESSION_LENGTH = (5, 10)
