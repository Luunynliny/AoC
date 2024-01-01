from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

dimensions = []

with open(puzzle) as f:
    for line in f.read().splitlines():
        dimensions.append(list(map(int, line.split("x"))))

wrapping_paper_area = 0

for length, width, height in dimensions:
    a = length * width
    b = width * height
    c = height * length

    wrapping_paper_area += 2 * (a + b + c) + min(a, b, c)

ic(wrapping_paper_area)

exec_time = perf_counter() - timer
ic(exec_time)
