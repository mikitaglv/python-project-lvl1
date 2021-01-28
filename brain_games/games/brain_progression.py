from random import randint


GAME_DESCRIPTION = "What number is missing in the progression?"


def make_progression():
    progression = []
    start_number = randint(1, 100)
    step = randint(1, 10)
    length = 10
    while len(progression) < length:
        progression.append(start_number)
        start_number += step
    return progression


def game_question():
    progression = make_progression()
    question_progression = []
    question_progression.extend(progression)
    hiden_index = randint(0, 9)
    question_progression[hiden_index] = ".."
    question_progression = " ".join(str(x) for x in question_progression)
    question = f"Question: {question_progression}"
    answer = progression[hiden_index]
    return (question, answer)
