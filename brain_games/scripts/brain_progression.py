#!/usr/bin/env python3
from brain_games.scripts.engine import get_username, play_engine
from brain_games.scripts.games.progression import progression_game, task_text


def main():
    username = get_username()
    play_engine(progression_game, username, task_text)


if __name__ == "__main__":
    main()