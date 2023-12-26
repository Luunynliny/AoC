from time import perf_counter

import numpy as np
from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()


with open(puzzle) as f:
    platerform = []

    for line in f.read().splitlines():
        platerform.append(list(line))

    platerform = np.array(platerform)

loads = np.arange(len(platerform), 0, -1)
total_load = 0

for row in platerform.T:
    head = 0
    tail = 0

    for i, c in enumerate(row):
        if c == "#":
            if i != 0:
                row[head:tail] = np.sort(row[head:tail])[::-1]

            head = i + 1
            tail = i + 1
            continue

        tail += 1

        if i == len(row) - 1 and tail != head:
            row[head : tail + 1] = np.sort(row[head : tail + 1])[::-1]

    total_load += np.sum(loads[np.argwhere(row == "O").flatten()])

ic(total_load)

exec_time = perf_counter() - timer
ic(exec_time)
