from itertools import pairwise
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

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

    extrapolation_sum += sum(s[-1] for s in sequences)

ic(extrapolation_sum)

exec_time = perf_counter() - timer
ic(exec_time)
