from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    number = randint(1, 100)
    question = f"Question: {number}"
    if is_even(number):
        answer = "yes"
    else:
        answer = "no"
    return (question, answer)


def is_even(number):
    if number % 2 == 0:
        return True
    return False
