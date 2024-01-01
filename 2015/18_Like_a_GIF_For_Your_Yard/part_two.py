from os import path
from time import perf_counter

import numpy as np
from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    grid = np.array(
        [[l == "#" for l in line] for line in f.read().splitlines()]
    )

S, _ = grid.shape


# https://stackoverflow.com/a/38157488
def neighbors(i, j):
    return (
        (i + a[0], j + a[1])
        for a in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        if ((0 <= i + a[0] < S) and (0 <= j + a[1] < S))
    )


for s in range(100):
    next_grid = grid.copy()

    for i, row in enumerate(grid):
        for j, is_on in enumerate(grid[i]):
            if (
                (i == 0 and j == 0)
                or (i == 0 and j == S - 1)
                or (i == S - 1 and j == 0)
                or (i == S - 1 and j == S - 1)
            ):
                continue

            neighbors_on_cnt = sum(grid[ni, nj] for ni, nj in neighbors(i, j))

            if is_on and neighbors_on_cnt not in [2, 3]:
                next_grid[i, j] = False
                continue

            if not is_on and neighbors_on_cnt == 3:
                next_grid[i, j] = True

    grid = next_grid

lights_on_cnt = np.sum(grid)

ic(lights_on_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
