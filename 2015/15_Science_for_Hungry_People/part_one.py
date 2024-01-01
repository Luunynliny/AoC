import re
from itertools import combinations
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    ingredient_specs = []

    for line in f.read().splitlines():
        _split = [s for s in re.split(" |,", line) if s]

        ingredient_specs.append(
            [
                int(_split[2]),
                int(_split[4]),
                int(_split[6]),
                int(_split[8]),
                int(_split[10]),
            ]
        )

    ingredient_specs = np.array(ingredient_specs)


# https://stackoverflow.com/a/52130135
def all_partitions(n, k):
    for c in combinations(range(n + k - 1), k - 1):
        yield np.array(
            [y - x - 1 for x, y in zip((-1,) + c, c + (n + k - 1,))]
        )


highest_score = 0

for p in all_partitions(100, len(ingredient_specs)):
    score = np.prod(
        np.sum(
            [p[i] * spec for i, spec in enumerate(ingredient_specs[:, :-1])],
            axis=0,
        ).clip(0)
    )
    highest_score = max(highest_score, score)

ic(highest_score)

exec_time = perf_counter() - timer
ic(exec_time)
