from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read()

seed_ranges_input, *maps_input = lines.split("\n\n")
seed_ranges = list(map(int, seed_ranges_input.split()[1:]))

seed_generator = (
    s
    for i in range(0, len(seed_ranges), 2)
    for s in range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1])
)

seeds = np.fromiter(seed_generator, int)
seeds_count = len(seeds)

for mi in maps_input:
    incr = np.zeros(seeds_count, dtype=int)

    for data in mi.split("\n")[1:]:
        dest, src, r = [int(n) for n in data.split()]

        mask = (src <= seeds) & (seeds <= src + (r - 1))
        incr[mask] = dest - src

    seeds += incr

ic(seeds.min())

exec_time = perf_counter() - timer
ic(exec_time)
