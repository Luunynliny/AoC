import re
from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read().splitlines()

nice_count = 0

for string in lines:
    if len(re.findall(r"(\w{2}).*?\1", string)) == 0:
        continue

    if len(re.findall(r"(\w)(\w)\1", string)) == 0:
        continue

    nice_count += 1

ic(nice_count)

exec_time = perf_counter() - timer
ic(exec_time)
