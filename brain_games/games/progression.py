from random import randint


def progression_generator(start:int, step:int) -> list[str]:
    max_lenght = 10
    progression = []
    progression.append(str(start))
    while len(progression) < max_lenght:
        next_number = int(progression[-1]) + step
        progression.append(str(next_number))
    return progression
    

def progression() -> str:
    start_prog = randint(1, 15)
    step_prog = randint(2, 5)
    heden_num_prog = randint(0, 9)
    progression = progression_generator(start_prog, step_prog)
    result, progression[heden_num_prog] = progression[heden_num_prog], '..'
    str_progression = ' '.join(progression)
    print(f"Question: {str_progression}")
    return result