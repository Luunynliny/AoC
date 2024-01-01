from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()

floor_number = sum([1 if c == "(" else -1 for c in line])

ic(floor_number)

exec_time = perf_counter() - timer
ic(exec_time)
