from random import randint


def progression():
    start_prog = randint(1, 15)
    step_prog = randint(2, 5)
    heden_num_prog = randint(0, 9)
    progression = []
    progression.append(str(start_prog))
    while len(progression) < 10:
        str_num = int(progression[-1]) + step_prog
        progression.append(str(str_num))
    result, progression[heden_num_prog] = progression[heden_num_prog], '..'
    str_progression = ', '.join(progression)
    print(f"Question: {str_progression}")
    return result