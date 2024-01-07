from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    sequences = []

    for line in f.read().splitlines():
        sequences.append(list(line))

button = 5
bathroom_code = ""

for sequence in sequences:
    for move in sequence:
        match move:
            case "U":
                button -= 3 if button not in (1, 2, 3) else 0
            case "D":
                button += 3 if button not in (7, 8, 9) else 0
            case "L":
                button -= 1 if button not in (1, 4, 7) else 0
            case "R":
                button += 1 if button not in (3, 6, 9) else 0

    bathroom_code += str(button)

ic(bathroom_code)

exec_time = perf_counter() - timer
ic(exec_time)
