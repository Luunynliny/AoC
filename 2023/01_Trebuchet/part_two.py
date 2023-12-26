import re
from time import perf_counter

from icecream import ic

example = "./example_two.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

calibration_sum = 0

regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
dgts = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    digits = re.findall(regex, line)
    first, last = digits[0], digits[-1]

    first = int(first) if len(first) == 1 else dgts.index(first) + 1
    last = int(last) if len(last) == 1 else dgts.index(last) + 1

    calibration_sum += first * 10 + last

ic(calibration_sum)

exec_time = perf_counter() - timer
ic(exec_time)
