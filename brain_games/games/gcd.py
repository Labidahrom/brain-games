import random


RULES_TEXT = "Find the greatest common divisor of given numbers."
INTERVAL_START = 1
INTERVAL_END = 100


def find_gcd(number1, number2):
    if min(number1, number2) == 0:
        return number1
    else:
        return find_gcd(min(number1, number2),
                        max(number1, number2) % min(number1, number2))


def generate_question_and_answer():
    number1 = random.randint(INTERVAL_START, INTERVAL_END)
    number2 = random.randint(INTERVAL_START, INTERVAL_END)
    result = str(find_gcd(number1, number2))
    question = f'{number1} {number2}'
    return question, result
