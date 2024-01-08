from collections import Counter
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    messages = []

    for line in f.read().splitlines():
        messages.append(list(line))

    messages = np.array(messages)

error_corrected_message = "".join(
    [Counter(col).most_common(1)[0][0] for col in messages.T]
)

ic(error_corrected_message)

exec_time = perf_counter() - timer
ic(exec_time)
