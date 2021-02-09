from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0 and i < num:
            return False
    return True


def game_question():
    number = randint(1, 100)
    question = f"Question: {number}"
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question, correct_answer)
