import random


task_text = "Find the greatest common divisor of given numbers."


def gcd_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = 0
    for i in range(1, min(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            result = str(i)
    question = f'Question: {number1} {number2}'
    return question, result


if __name__ == "__main__":
    gcd_game()
