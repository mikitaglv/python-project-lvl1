from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0 and i < num:
            return False
    return True


def get_question_answer():
    number = randint(1, 100)
    question = f"Question: {number}"
    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"
    return (question, answer)
