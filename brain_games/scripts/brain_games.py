#!/usr/bin/env python3
from brain_games import cli

def main():
    print("Welcome to the Brain Games!")
    user_name = cli.ask_question("May I have your name? ")
    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()
