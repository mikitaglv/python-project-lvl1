from random import randint
from brain_games.engine import greeting


def is_prime(num):
    for i in range(2, num):
        if num % i == 0 and i < num:
            return "no"
    return "yes"


def game_question():
    print('Answer "yes" if the number is prime , otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = randint(1, 1000)
        print(f"Question: {number}")
        answer = input("Your answer: ")
        if str(answer) != is_prime(number):
            print(f"{answer} is wrong answer. Lets try again")
            counter = 0
            continue
        else:
            print("Correct")
            counter += 1


def run_brain_prime():
    user_name = greeting()
    game_question()
    print(f"Congratulations, {user_name}")
