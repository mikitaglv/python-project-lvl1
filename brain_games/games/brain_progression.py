from random import randint
from brain_games.engine import greeting


def make_progression():
    progression = []
    start_number = randint(1, 100)
    step = randint(1, 10)
    length = 10
    while len(progression) < length:
        progression.append(start_number)
        start_number += step
    return progression


def game_question():
    print("Shat number is missing in the progression?")
    counter = 0
    while counter < 3:
        progression = make_progression()
        question_progression = []
        question_progression.extend(progression)
        hiden_index = randint(0, 9)
        question_progression[hiden_index] = ".."
        print(f"Question: {question_progression}")
        correct_answer = progression[hiden_index]
        user_answer = input("Your answer: ")
        if int(user_answer) != correct_answer:
            print(f"{user_answer} is wrong answer. Lets try again")
            counter = 0
            continue
        else:
            print("Correct")
            counter += 1


def run_brain_progression():
    user_name = greeting()
    game_question()
    print(f"Congratulations, {user_name}")
