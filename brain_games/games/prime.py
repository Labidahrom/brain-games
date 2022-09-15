import random


RULES_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
INTERVAL_START = 1
INTERVAL_END = 100


def is_prime(number):
    if number <= 1:
        return False
    elif 2 >= number > 4:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def generate_question_and_answer():
    number = random.randint(INTERVAL_START, INTERVAL_END)
    question = f'{number}'
    if is_prime(number):
        result = "yes"
    else:
        result = "no"
    return question, result
