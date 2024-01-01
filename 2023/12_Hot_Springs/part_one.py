from itertools import combinations
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read().splitlines()

arrangement_cnt_sum = 0

for line in lines:
    springs, groups = line.split()
    groups = [int(g) for g in groups.split(",")]

    unknown_idx = [i for i, c in enumerate(springs) if c == "?"]
    damaged_spring_to_find_cnt = sum(groups) - springs.count("#")

    for p in combinations(unknown_idx, damaged_spring_to_find_cnt):
        config = "".join(
            [
                "#" if i in p else "." if i in unknown_idx else c
                for i, c in enumerate(springs)
            ]
        )

        if [len(g) for g in config.split(".") if g] == groups:
            arrangement_cnt_sum += 1

ic(arrangement_cnt_sum)

exec_time = perf_counter() - timer
ic(exec_time)
