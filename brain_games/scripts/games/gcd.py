import random
import prompt


task_text = "Find the greatest common divisor of given numbers."


def gcd_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    max_mul = 0
    for i in range(1, min(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            max_mul = i
    print(f'Question: {number1} {number2}')
    user_answer = int(prompt.integer(('Your answer: ')))
    if user_answer == max_mul:
        print('Correct!')
        return True
    else:
        print(f"Question: {number1} {number2}\nYour answer: {user_answer}\n"
              f"{user_answer} is wrong answer ;(. Correct answer was "
              f"{max_mul}.")
        return False


if __name__ == "__main__":
    gcd_game()
