#!/usr/bin python
"""This module runs welcome_user function."""
from engine import get_username, play_engine
from games.calc import calc_game, task_text


def main():
    username = get_username()
    play_engine(calc_game, username, task_text)


if __name__ == "__main__":
    main()
