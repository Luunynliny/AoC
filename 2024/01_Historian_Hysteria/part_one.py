from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_one.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    right = []
    left = []

    for line in f.readlines():
        r, l = line.split()

        right.append(int(r))
        left.append(int(l))

distance = sum([abs(r - l ) for r, l in zip(sorted(right), sorted(left))])

ic(distance)

exec_time = perf_counter() - timer
ic(exec_time)
