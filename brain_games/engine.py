from random import randint
from brain_games import cli

def greeting():
    print('Welcome to the Brain Games!')
    user_name = cli.get_user_name()
    print(f'Hello, {user_name}')
    return user_name
