from os import path
from time import perf_counter
import numpy as np

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_one.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    array = np.array([list(line.strip()) for line in f.readlines()])

xmas_cnt = 0

for i in range(array.shape[0]):
    xmas_cnt += "".join(array[i]).count("XMAS")
    xmas_cnt += "".join(array[i][::-1]).count("XMAS")

for j in range(array.shape[1]):
    xmas_cnt += "".join(array[:, j]).count("XMAS")
    xmas_cnt += "".join(array[:, j][::-1]).count("XMAS")

for off in range(-array.shape[1] + 1, array.shape[0]):
    xmas_cnt += "".join(array.diagonal(offset=off)).count("XMAS")
    xmas_cnt += "".join(array.diagonal(offset=off)[::-1]).count("XMAS")

    xmas_cnt += "".join(np.flipud(array.diagonal(offset=off))).count("XMAS")
    xmas_cnt += "".join(np.flipud(array.diagonal(offset=off))[::-1]).count("XMAS")

ic(xmas_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
