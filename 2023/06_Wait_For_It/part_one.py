from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

ways_product = 1

for i, t in enumerate(times):
    wins_count = 0

    for d in ((t - h) * h for h in range(t + 1)):
        if d > distances[i]:
            wins_count += 1

    ways_product *= wins_count

ic(ways_product)

exec_time = perf_counter() - timer
ic(exec_time)
