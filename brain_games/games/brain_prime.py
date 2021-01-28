from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def correct_answer(num):
    for i in range(2, num):
        if num % i == 0 and i < num:
            return "no"
    return "yes"


def game_question():
    number = randint(1, 100)
    question = f"Question: {number}"
    answer = correct_answer(number)
    return (question, answer)
