import prompt


def play_engine(game):
    username = prompt.string('Welcome to the Brain Games!\n'
                             'May I have your name? ')
    print(f"Hello, {username}!")
    print(game.task_text)
    for i in range(3):
        question, result = game.game()
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


if __name__ == "__main__":
    play_engine()
