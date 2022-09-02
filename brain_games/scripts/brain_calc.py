#!/usr/bin python
"""This module runs welcome_user function."""
from brain_games.scripts.engine import get_username, play_engine
from brain_games.scripts.games.calc import calc_game, task_text


def main():
    username = get_username()
    play_engine(calc_game, username, task_text)


if __name__ == "__main__":
    main()
