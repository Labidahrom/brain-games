import random


task_text = "What number is missing in the progression?"


def progression_game():
    progression_start = random.randint(1, 100)
    progression_step = random.randint(2, 6)
    progression_list = [str(progression_start + (i * progression_step))
                        for i in range(random.randint(5, 10))]
    index_to_replace = random.randint(0, len(progression_list) - 1)
    result = progression_list[index_to_replace]
    progression_list[index_to_replace] = '..'
    progression_string = ' '.join(progression_list)
    question = f"Question: {progression_string}"
    return question, result


if __name__ == "__main__":
    progression_game()
