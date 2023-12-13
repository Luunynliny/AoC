from time import perf_counter

import numpy as np
from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()


with open(puzzle) as f:
    patterns = []
    buff = []

    lines = f.read().splitlines()

    for i, line in enumerate(lines):
        if i == 0 or line == "":
            patterns.append([])

        if line == "":
            continue

        patterns[-1].append(list(line))


def search_reflection(arr: np.ndarray) -> int | None:
    row_max = arr.shape[0]

    for r in range(1, row_max):
        size = min(r, row_max - r)
        sub = arr[r - size : r + size]

        sub_a = np.flipud(sub[: len(sub) // 2])
        sub_b = sub[len(sub) // 2 :]

        if np.sum(sub_a == sub_b) == np.prod(sub_a.shape) - 1:
            return r

    return None


summary = 0

for pattern in patterns:
    p = np.array(pattern)

    n = search_reflection(p.T)

    if n is None:
        n = search_reflection(p) * 100

    summary += n

ic(summary)

exec_time = perf_counter() - timer
ic(exec_time)
