from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()

floor_number = 0
basement_enter_position = 0

for i, c in enumerate(line):
    floor_number += 1 if c == "(" else -1

    if floor_number == -1:
        basement_enter_position = i + 1
        break

ic(basement_enter_position)

exec_time = perf_counter() - timer
ic(exec_time)
