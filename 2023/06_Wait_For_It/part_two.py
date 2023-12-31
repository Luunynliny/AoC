from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

wins_count = 0

for d in ((time - h) * h for h in range(time + 1)):
    if d > distance:
        wins_count += 1

ic(wins_count)

exec_time = perf_counter() - timer
ic(exec_time)
