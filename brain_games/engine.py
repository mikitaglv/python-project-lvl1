from brain_games import cli


ROUNDS = 3


def greeting():
    print("Welcome to the Brain Games!")
    user_name = cli.get_user_name()
    print(f"Hello, {user_name}!")
    return user_name


def game_engine(game=None):
    user_name = greeting()
    print(game.GAME_DESCRIPTION)
    counter = 0
    while counter < ROUNDS:
        question, correct_answer = game.game_question()
        print(question)
        user_answer = input("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            counter += 1
        else:
            print(f"Let's try again, {user_name}!")
            return None
    print(f"Congratulations, {user_name}!")


def run(game):
    game_engine(game)
