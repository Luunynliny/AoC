from itertools import product
from time import perf_counter

import numpy as np
from icecream import ic

puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    containers = np.array([int(line) for line in f.read().splitlines()])

combinations_cnt = 0

for mask in product([False, True], repeat=len(containers)):
    if np.sum(containers[np.array(mask)]) == 150:
        combinations_cnt += 1

ic(combinations_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
