from itertools import product
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    containers = np.array([int(line) for line in f.read().splitlines()])

min_nb_container = np.Infinity
combinations_cnt = 0

for mask in product([False, True], repeat=len(containers)):
    if np.sum(containers[np.array(mask)]) == 150:
        if (nb := np.sum(mask)) < min_nb_container:
            min_nb_container = nb
            combinations_cnt = 0

        if nb == min_nb_container:
            combinations_cnt += 1

ic(combinations_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
