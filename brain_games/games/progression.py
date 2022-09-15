import random


RULES_TEXT = "What number is missing in the progression?"
PROGRESSION_INT_START = 1
PROGRESSION_INT_END = 100
DIFFERENCE_INT_START = 2
DIFFERENCE_INT_END = 6
LENGTH_INT_START = 5
LENGTH_INT_END = 10
GENERATE_INDEX_START = 0


def generate_progression(initial_term, difference, length):
    progression = [initial_term + (i * difference) for i in range(length)]
    return progression


def generate_missing_item_index(length):
    index_to_replace = random.randint(GENERATE_INDEX_START, length - 1)
    return index_to_replace


def get_missing_item(progression, index):
    return str(progression[index])


def convert_to_str(progression, index_to_replace):
    progression_string = ''
    progression[index_to_replace] = '..'
    for i in progression:
        progression_string = progression_string + str(i) + ' '
    output = progression_string.strip()
    return output


def generate_question_and_answer():
    initial_term = random.randint(PROGRESSION_INT_START, PROGRESSION_INT_END)
    difference = random.randint(DIFFERENCE_INT_START, DIFFERENCE_INT_END)
    length = random.randint(LENGTH_INT_START, LENGTH_INT_END)
    progression = generate_progression(initial_term, difference, length)
    index_to_replace = generate_missing_item_index(len(progression))
    result = get_missing_item(progression, index_to_replace)
    question = f"{convert_to_str(progression, index_to_replace)}"
    return question, result
