import random


task_text = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    generate_number = random.randint(1, 1000)
    question = f'Question: {generate_number}'
    if generate_number % 2 == 0:
        result = "yes"
    else:
        result = "no"
    return question, result


if __name__ == "__main__":
    even_game()
