import prompt


ROUNDS_NUMBER = 3
WELCOME_MESSAGE = 'Welcome to the Brain Games!\nMay I have your name? '


def run_game(game):
    username = prompt.string(WELCOME_MESSAGE)
    print(f"Hello, {username}!")
    print(game.RULES_TEXT)
    for i in range(ROUNDS_NUMBER):
        question, result = game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.\nLet's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
