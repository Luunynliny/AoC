from itertools import pairwise
from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

histories = []

with open(puzzle) as f:
    for line in f.read().splitlines():
        histories.append(list(map(int, line.split())))

extrapolation_sum = 0

for history in histories:
    sequences = [history]

    while len(set(sequences[-1])) > 1:
        sequences.append([b - a for a, b in pairwise(sequences[-1])])

    extrapolation_sum += sum(
        s[0] if i % 2 == 0 else -s[0] for i, s in enumerate(sequences)
    )

ic(extrapolation_sum)

exec_time = perf_counter() - timer
ic(exec_time)
