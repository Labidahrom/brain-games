#!/usr/bin python
"""This module runs welcome_user function."""
from engine import get_username, play_engine
from games.even import even_game, task_text


username = get_username()
play_engine(even_game, username, task_text)