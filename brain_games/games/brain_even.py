from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    number = randint(1, 100)
    question = f"Question: {number}"
    correct_answer = is_even(number)
    return (question, correct_answer)


def is_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"
