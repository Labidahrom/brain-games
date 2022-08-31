#!/usr/bin python
"""This module runs welcome_user function."""
import random
import prompt


def main():
    username = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {username}!\nWhat is the result of the expression?')
    n = 3
    while True and n > 0:
        operation_type = '+-*'[random.randint(0, 2)]
        member_1 = random.randint(1, 1000)
        member_2 = random.randint(1, 1000)
        if operation_type == '+':
            print(f'Question: {member_1} + {member_2}')
            math_result = member_1 + member_2
        elif operation_type == '-':
            print(f'Question: {member_1} - {member_2}')
            math_result = member_1 - member_2
        elif operation_type == '*':
            print(f'Question: {member_1} * {member_2}')
            math_result = member_1 * member_2
        user_answer = int(prompt.integer(('Your answer: ')))
        if user_answer == math_result:
            print('Correct!')
            n -= 1
        else:
            print(f"Question: {member_1} {operation_type} {member_2}\nYour answer: {user_answer}\n"
                  f"{user_answer} is wrong answer ;(. Correct answer was {math_result}.\n"
                  f"\nLet's try again, {username}")
            return False
    print(f"Congratulations, {username}!")

if __name__ == "__main__":
    main()
