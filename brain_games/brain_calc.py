from random import randint
from brain_games.engine import greeting


def game_question():
    print('What is the resul of the expression?')

    counter = 0
    while counter < 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        random_calculation = randint(1, 3)
        if random_calculation == 1:
            result = first_number + second_number
            print(f'Question: {first_number} + {second_number}')
            answer = input('Your answer: ')
        elif random_calculation == 2:
            result = first_number - second_number
            print(f'Question: {first_number} - {second_number}')
            answer = input('Your answer: ')
        elif random_calculation == 3:
            result = first_number * second_number
            print(f'Question: {first_number} * {second_number}')
            answer = input('Your answer: ')
        if result == int(answer):
            print('Correct!')
            counter += 1
            continue
        else:
            print('Let\'s try again!')
            counter = 0
            continue


def run_brain_calc():
    user_name = greeting()
    game_question()
    print(f'Congratulations, {user_name}')
