#!/usr/bin python
"""This module runs welcome_user function."""
import random
import prompt


task_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game():
    number = random.randint(1, 100)
    is_prime = 'yes'
    if number == 1:
        is_prime = 'no'
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = 'no'
                break
    print(f'Question: {number}')
    user_answer = input('Your answer: ')
    if user_answer == is_prime:
        print('Correct!')
        return True
    else:
        print(f"Question: {number}\nYour answer: {user_answer}\n"
              f"'{user_answer}' is wrong answer ;(. Correct answer was '{is_prime}'.")
        return False








