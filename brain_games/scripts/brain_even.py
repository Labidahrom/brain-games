#!/usr/bin python
"""This module runs welcome_user function."""
import random
import prompt


def main():
    username = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {username}!")
    n = 3
    while True and n > 0:
        generate_number = random.randint(1, 1000)
        print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion {generate_number}')
        user_answer = input('Your answer: ')
        if (generate_number % 2 == 0 and user_answer == 'yes') or (generate_number % 2 == 1 and
        user_answer == 'no'):
            print('Correct!')
            n -= 1
        elif generate_number % 2 == 0 and user_answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {username}!")
            return False
        elif generate_number % 2 == 1 and user_answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {username}!")
            return False
        else:
            print('This is wrong answer! You answer must be "no" or "yes"')
            return False
    if n == 0:
        print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
