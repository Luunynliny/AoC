import re
from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    olds = []
    news = []

    skip = False

    for line in f.read().splitlines():
        if line == "":
            skip = True

        if skip:
            seed = line
            continue

        o, n = line.split(" => ")

        olds.append(o)
        news.append(n)

distinct_molecules_cnt = len(
    set(
        [
            r
            for i in range(len(olds))
            for r in [
                seed[: m.start()] + news[i] + seed[m.end() :]
                for m in re.finditer(olds[i], seed)
            ]
        ]
    )
)

ic(distinct_molecules_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
