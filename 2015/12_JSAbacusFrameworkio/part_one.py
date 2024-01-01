import re
from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()

number_sum = sum([int(n) for n in re.findall(r"-?(?:\d+)+", line)])

ic(number_sum)

exec_time = perf_counter() - timer
ic(exec_time)
