import random


RULES_TEXT = "What is the result of the expression?"
INTERVAL_START = 1
INTERVAL_END = 10
ARITHMETIC_SIGNS = ['+', '-', '*']


def generate_question_and_answer():
    operation_type = random.choice(ARITHMETIC_SIGNS)
    member_1 = random.randint(INTERVAL_START, INTERVAL_END)
    member_2 = random.randint(INTERVAL_START, INTERVAL_END)
    if operation_type == '+':
        result = member_1 + member_2
    elif operation_type == '-':
        result = member_1 - member_2
    elif operation_type == '*':
        result = member_1 * member_2
    question = f'{member_1} {operation_type} {member_2}'
    result = str(result)
    return question, result
