import prompt


def play_engine(game):
    username = prompt.string('Welcome to the Brain Games!\n'
                             'May I have your name? ')
    ROUNDS_NUMBER = 3
    print(f"Hello, {username}!")
    print(game.RULES_TEXT)
    for i in range(ROUNDS_NUMBER):
        question, result = game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == result:
            print('Correct!')
        else:
            print(f'Question: {question}\nYour answer: {user_answer}\n'
                  f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.\nLet's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
