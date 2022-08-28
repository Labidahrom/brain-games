#!/usr/bin python
"""This module runs welcome_user function."""
from brain_games.cli import welcome_user


def main():
    print(f"Hello, {welcome_user()}!")


if __name__ == "__main__":
    main()
