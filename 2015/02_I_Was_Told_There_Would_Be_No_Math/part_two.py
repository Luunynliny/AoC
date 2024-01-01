from time import perf_counter

from icecream import ic

puzzle = "./puzzle.txt"

timer = perf_counter()

dimensions = []

with open(puzzle) as f:
    for line in f.read().splitlines():
        dimensions.append(list(map(int, line.split("x"))))

ribbon_length = sum(
    [
        min(2 * (l + w), 2 * (w + h), 2 * (h + l)) + (l * w * h)
        for l, w, h in dimensions
    ]
)

ic(ribbon_length)

exec_time = perf_counter() - timer
ic(exec_time)
