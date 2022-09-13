import random


task_text = "What number is missing in the progression?"


def calculate_progression(initial_term, difference, length):
    progression_list = [str(initial_term + (i * difference))
                        for i in range(length)]
    return progression_list


def convert_to_str(progression_list):
    progression_string = ' '.join(progression_list)
    return progression_string


def game():
    initial_term = random.randint(1, 100)
    difference = random.randint(2, 6)
    length = random.randint(5, 10)
    progression_list = calculate_progression(initial_term, difference, length)
    index_to_replace = random.randint(0, len(progression_list) - 1)
    result = progression_list[index_to_replace]
    progression_list[index_to_replace] = '..'
    progression_string = convert_to_str(progression_list)
    question = f"{progression_string}"
    return question, result
