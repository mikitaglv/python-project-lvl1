from random import randint


print('Welcome to the Brain Games!')


name = input('May I have your name? ')
print(f'Hello, {name}!')


def game_question():
    number = randint(1, 100)
    print('Answer "yes" if the number is even , otherwise answer "no".')
    print(f'Question: {number}')
    answer = input('Your answer: ')
    while answer != correct_answer(number):
        print(f'{answer} is wrong answer. Lets try again, {name}')
        answer = input('Your answer: ')
    print('Correct!')


def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
