#!/usr/bin python
"""This module runs welcome_user function."""
import random
import prompt


task_text = "What is the result of the expression?"

def calc_game():
    operation_type = '+-*'[random.randint(0, 2)]
    member_1 = random.randint(1, 10)
    member_2 = random.randint(1, 10)
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
        return True
    else:
        print(f"Question: {member_1} {operation_type} {member_2}\nYour answer: {user_answer}\n"
              f"{user_answer} is wrong answer ;(. Correct answer was {math_result}.")
        return False


if __name__ == "__main__":
    calc_game()