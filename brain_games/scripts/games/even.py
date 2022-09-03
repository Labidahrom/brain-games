import random


task_text = "Answer 'yes' if the number is even, otherwise answer 'no'."


def even_game():
    generate_number = random.randint(1, 1000)
    print(f'Question: {generate_number}')
    user_answer = input('Your answer: ')
    if (generate_number % 2 == 0 and user_answer == 'yes') or \
            (generate_number % 2 == 1 and user_answer == 'no'):
        print('Correct!')
        return True
    elif generate_number % 2 == 0 and user_answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    elif generate_number % 2 == 1 and user_answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
    else:
        print('This is wrong answer! You answer must be "no" or "yes"')
        return False


if __name__ == "__main__":
    even_game()
