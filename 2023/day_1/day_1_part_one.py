import re

example = "./part_one_example.txt"
puzzle = "./puzzle.txt"

with open(puzzle) as f:
    lines = f.readlines()

calibration_sum = 0

for line in lines:
    digits = re.findall(r"\d", line)

    if len(digits) == 1:
        calibration_sum += int(digits[0]) * 11
    else:
        calibration_sum += int(digits[0]) * 10 + int(digits[-1])

print(calibration_sum)
