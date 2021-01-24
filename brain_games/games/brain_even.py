from random import randint
from brain_games.engine import greeting


def game_question():
    print('Answer "yes" if the number is even , otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")
        if answer != correct_answer(number):
            print(f"{answer} is wrong answer. Lets try again")
            counter = 0
            continue
        else:
            print("Correct")
            counter += 1


def correct_answer(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def run_brain_even():
    user_name = greeting()
    game_question()
    print(f"Congratulations, {user_name}")
