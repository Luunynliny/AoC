from os import path
from time import perf_counter
import re

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

result = 0

for line in lines:
    matches= re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

    for mult in matches:
        a, b = re.findall(r"(\d+)", mult)
        result += int(a) * int(b)

ic(result)

exec_time = perf_counter() - timer
ic(exec_time)
