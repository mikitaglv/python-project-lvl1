from random import randint


GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def game_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f"Question: {number1} {number2}"
    answer = gcd(number1, number2)
    return (question, str(answer))


def gcd(num1, num2):
    result = 1
    counter = 1
    while counter <= num1 and counter <= num2:
        if num1 % counter == 0 and num2 % counter == 0:
            result = counter
        counter += 1
    return result
