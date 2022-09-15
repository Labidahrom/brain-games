import random


RULES_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
INTERVAL_START = 1
INTERVAL_END = 1000


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    number = random.randint(INTERVAL_START, INTERVAL_END)
    question = f'{number}'
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    return question, result
