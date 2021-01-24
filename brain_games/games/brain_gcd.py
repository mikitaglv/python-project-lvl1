from random import randint
from brain_games.engine import greeting


def game_question():
    print("Find the greatest common divisor of given numbers.")
    counter = 0
    while counter < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f"Question: {number1} {number2}")
        answer = input("Your answer: ")
        correct_answer = gcd(number1, number2)
        if int(answer) != correct_answer:
            print(f"{answer} is wrong answer. Lets try again")
            counter = 0
            continue
        else:
            print("Correct")
            counter += 1


def gcd(num1, num2):
    result = 1
    counter = 1
    while counter <= num1 and counter <= num2:
        if num1 % counter == 0 and num2 % counter == 0:
            result = counter
        counter += 1
    return result


def run_brain_gcd():
    user_name = greeting()
    game_question()
    print(f"Congratulations, {user_name}")
