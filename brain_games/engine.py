from brain_games import cli


ROUNDS = 3


def run(game):
    print("Welcome to the Brain Games!")
    user_name = cli.ask_question("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(game.GAME_DESCRIPTION)
    counter = 0
    while counter < ROUNDS:
        question, answer = game.get_question_answer()
        print(question)
        user_answer = cli.ask_question("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            counter += 1
        else:
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
