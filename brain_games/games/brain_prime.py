from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(num):
    for i in range(2, num):
        if num % i == 0 and i < num:
            return True
    return False


def game_question():
    number = randint(1, 100)
    question = f"Question: {number}"
    if is_prime(number):
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return (question, correct_answer)
