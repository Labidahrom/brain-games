import prompt


def welcome_user():
    """Return message with user name."""
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    return name


if __name__ == '__main__':
    welcome_user()
