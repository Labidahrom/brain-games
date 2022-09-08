import random


task_text = "What is the result of the expression?"


def game():
    operation_type = '+-*'[random.randint(0, 2)]
    member_1 = random.randint(1, 10)
    member_2 = random.randint(1, 10)
    if operation_type == '+':
        question = f'{member_1} + {member_2}'
        result = member_1 + member_2
    elif operation_type == '-':
        question = f'{member_1} - {member_2}'
        result = member_1 - member_2
    elif operation_type == '*':
        question = f'{member_1} * {member_2}'
        result = member_1 * member_2
    result = str(result)
    return question, result

