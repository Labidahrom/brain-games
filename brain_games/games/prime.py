import random


task_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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


def game():
    number = random.randint(1, 100)
    question = f'{number}'
    if is_prime(number):
        result = "yes"
    else:
        result = "no"
    return question, result

