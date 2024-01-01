import re
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_one.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

calibration_sum = 0

for line in lines:
    digits = re.findall(r"\d", line)

    if len(digits) == 1:
        calibration_sum += int(digits[0]) * 11
    else:
        calibration_sum += int(digits[0]) * 10 + int(digits[-1])

ic(calibration_sum)

exec_time = perf_counter() - timer
ic(exec_time)
