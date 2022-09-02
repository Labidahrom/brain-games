import random
import prompt


def get_username():
    username = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {username}!")
    return username


def play_engine(game, username, task_text):
    print(task_text)
    for i in range(3):
        if not game():
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    play_engine()
    get_username()
