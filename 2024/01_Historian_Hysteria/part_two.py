from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    left = []
    right = []

    for line in f.readlines():
        l, r = line.split()

        left.append(int(l))
        right.append(int(r))

similarity_score = sum([l * right.count(l) for l in left])

ic(similarity_score)

exec_time = perf_counter() - timer
ic(exec_time)
