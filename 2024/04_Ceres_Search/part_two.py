from os import path
from time import perf_counter
import numpy as np

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    array = np.array([list(line.strip()) for line in f.readlines()])

a_indices = list(zip(*np.where(array == "A")))
xmas_cnt = 0

for idx in a_indices:
    a = idx[0] - 1, idx[1] - 1
    b = idx[0] - 1, idx[1] + 1
    c = idx[0] + 1, idx[1] + 1
    d = idx[0] + 1, idx[1] - 1

    is_outbound = False
    for cell in (a, b, c, d):
        if not 0 <= cell[0] < array.shape[0]:
            is_outbound = True
            break

        if not 0 <= cell[1] < array.shape[1]:
            is_outbound = True
            break

    if not is_outbound:
        xmas_cnt += int(array[a] + array[b] + array[c] + array[d] in ("MMSS", "SMMS", "SSMM", "MSSM"))

ic(xmas_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
