import re
from time import perf_counter

from icecream import ic

example = "./example_one.txt"
puzzle = "./puzzle.txt"

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
