#!/usr/bin/env python3
from brain_games.engine import play_engine
from brain_games.games import gcd


def main():
    play_engine(gcd)


if __name__ == "__main__":
    main()
