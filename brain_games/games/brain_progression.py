from random import randint


GAME_DESCRIPTION = "What number is missing in the progression?"


def make_progression(start, step, length):
    progression = []
    while len(progression) < length:
        progression.append(start)
        start += step
    return progression


def game_question():
    start = randint(1, 100)
    step = randint(1, 10)
    length = 10
    progression = make_progression(start, step, length)
    question_progression = []
    question_progression.extend(progression)
    hiden_index = randint(0, 9)
    question_progression[hiden_index] = ".."
    question_progression = " ".join(str(x) for x in question_progression)
    question = f"Question: {question_progression}"
    answer = progression[hiden_index]
    return (question, str(answer))
