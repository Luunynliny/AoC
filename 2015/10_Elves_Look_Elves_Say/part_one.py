import re
from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()

for i in range(40):
    line = "".join(
        [f"{len(a+b)}{a}" for a, b in re.findall(r"(\d)(\1*)", line)]
    )

result_length = len(line)

ic(result_length)

exec_time = perf_counter() - timer
ic(exec_time)
