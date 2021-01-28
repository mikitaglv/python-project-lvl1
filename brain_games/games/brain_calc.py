from random import randint, choice
import operator


GAME_DESCRIPTION = "What is the result of the expression?"


operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def random_operation():
    return choice(list(operations.keys()))


def correct_answer(first_number, second_number, operation):
    return str(operations[operation](first_number, second_number))


def game_question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operation = random_operation()
    question = f"Question: {first_number} {operation} {second_number}"
    answer = correct_answer(first_number, second_number, operation)
    return (question, answer)
