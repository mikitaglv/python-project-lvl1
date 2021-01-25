from random import randint


GAME_DESCRIPTION = "What is the resul of the expression?"


def game_question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    random_calculation = randint(1, 3)
    if random_calculation == 1:
        correct_answer = first_number + second_number
        question = f"Question: {first_number} + {second_number}"
    elif random_calculation == 2:
        correct_answer = first_number - second_number
        question = f"Question: {first_number} - {second_number}"
    elif random_calculation == 3:
        correct_answer = first_number * second_number
        question = f"Question: {first_number} * {second_number}"
    return (question, correct_answer)
