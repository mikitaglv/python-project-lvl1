#!/usr/bin/env python3

from brain_games import brain_even

def greet():
    print('Welcome to the Brain Games!')


def main():
    brain_even.game_question()
    brain_even.game_question()
    brain_even.game_question()
    print(f'Congratulations, {brain_even.name}')


if __name__ == '__main__':
    main()
