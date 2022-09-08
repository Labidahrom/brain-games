import random


task_text = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game():
    number = random.randint(1, 1000)
    question = f'{number}'
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    return question, result
