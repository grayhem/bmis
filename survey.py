"""
results are stored in the data directory with today's date and time in UTC
"""

import json
import datetime

import numpy as np

RESULTS_DIR = "data/"
PROMPTS = [
    "lively",
    "happy",
    "sad",
    "tired",
    "caring",
    "content",
    "gloomy",
    "jittery",
    "drowsy",
    "grouchy",
    "peppy",
    "nervous",
    "calm",
    "loving",
    "fed up",
    "active"
]
SCALE = "? 0->3 :::"
FEELING = "how much are you feeling:"
TAB = "    "
PROMPT_RANGE = (0, 3)
OVERALL = "overall, your mood is? -10 -> 10 :::"
OVERALL_RANGE = (-10, 10)


def do_prompt(this_prompt):
    """
    with input checking
    """
    value = int(input(TAB + this_prompt + SCALE))
    while value < PROMPT_RANGE[0] or value > PROMPT_RANGE[1]:
        print("value must fit range", PROMPT_RANGE)
        value = int(input(TAB + this_prompt + SCALE))
    return value


def do_overall():
    """
    """
    value = int(input(OVERALL))
    while value < OVERALL_RANGE[0] or value > OVERALL_RANGE[1]:
        print("value must fit range", OVERALL_RANGE)
        value = int(input(OVERALL))
    return value


def value_wrap(fn, *args):
    """
    pure jank
    """
    try:
        return fn(*args)
    except ValueError as e:
        print(e)
        return value_wrap(fn, *args)


def save(result):
    """
    """
    name = RESULTS_DIR + datetime.datetime.utcnow().isoformat()
    name = name.replace(":", "_")
    with open(name, "w") as the_file:
        json.dump(result, the_file, sort_keys=True, indent=4)


def random_survey():
    """
    ye
    """
    print(FEELING)
    result = {}
    for this_prompt in np.random.permutation(PROMPTS):
        result[this_prompt] = value_wrap(do_prompt, this_prompt)

    result["overall"] = value_wrap(do_overall)
    save(result)



if __name__ == '__main__':
    random_survey()
