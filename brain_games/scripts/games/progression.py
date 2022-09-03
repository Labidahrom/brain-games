#!/usr/bin python
"""This module runs welcome_user function."""
import random
import prompt


task_text = "What number is missing in the progression?"


def progression_game():
    progression_start = random.randint(1, 100)
    progression_step = random.randint(2, 6)
    progression_list = [str(progression_start + (i * progression_step))
                        for i in range(1, random.randint(5, 10))]
    index_to_replace = random.randint(0, len(progression_list) - 1)
    missing_item = progression_list[index_to_replace]
    progression_list[index_to_replace] = '..'
    progression_string = ' '.join(progression_list)
    print(progression_string)
    user_answer = int(prompt.integer('Your answer: '))
    if user_answer == int(missing_item):
        print('Correct!')
        return True
    else:
        print(f"Question: {progression_string}\nYour answer: {user_answer}\n"
              f"'{user_answer}' in wrong answer ;(. Correct answer was '{missing_item}'.")
        return False








