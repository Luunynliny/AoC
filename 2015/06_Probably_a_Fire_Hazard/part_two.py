import re
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

instructions = []

with open(puzzle) as f:
    for line in f.read().splitlines():
        l_split = re.split(" |,", line)

        if len(l_split) == 7:
            l_split.pop(0)

        instructions.append(
            (
                l_split[0],
                (int(l_split[1]), int(l_split[2])),
                (int(l_split[-2]), int(l_split[-1])),
            )
        )

grid = np.full((1_000, 1_000), 0, dtype=int)

for instruction in instructions:
    cmd, a, b = instruction

    match cmd:
        case "on":
            grid[a[0] : b[0] + 1, a[1] : b[1] + 1] += 1
        case "off":
            grid[a[0] : b[0] + 1, a[1] : b[1] + 1] -= 1
        case "toggle":
            grid[a[0] : b[0] + 1, a[1] : b[1] + 1] += 2

    grid[grid < 0] = 0

total_brightness = grid.sum()

ic(total_brightness)

exec_time = perf_counter() - timer
ic(exec_time)
