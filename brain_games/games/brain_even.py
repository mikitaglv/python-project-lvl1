from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    number = randint(1, 100)
    question = f"Question: {number}"
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"
