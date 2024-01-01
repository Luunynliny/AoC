from itertools import combinations
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read().splitlines()

image = np.array([list(l) for l in lines])
galaxy_ys, galaxy_xs = np.where(image == "#")

expansion_xs = np.where((image == ".").all(axis=0))[0]
expansion_ys = np.where((image[:, 1:] == image[:, :-1]).all(axis=1))[0]

for x in expansion_xs[::-1]:
    galaxy_xs[galaxy_xs > x] += 999_999

for y in expansion_ys[::-1]:
    galaxy_ys[galaxy_ys > y] += 999_999

shortest_path_sum = sum(
    [
        abs(u[0] - v[0]) + abs(u[1] - v[1])
        for u, v in combinations(zip(galaxy_ys, galaxy_xs), 2)
    ]
)

ic(shortest_path_sum)

exec_time = perf_counter() - timer
ic(exec_time)
