import random


task_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game():
    number = random.randint(1, 100)
    result = 'yes'
    if number == 1:
        result = 'no'
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                result = 'no'
                break
    question = f'Question: {number}'
    return question, result


if __name__ == "__main__":
    prime_game()
