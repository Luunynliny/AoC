from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

safe_reports_cnt = 0

for line in lines:
    report = list(map(int, line.split()))
    is_safe = True

    if sorted(report) == report or sorted(report, reverse=True) == report:
        for i in range(len(report) - 1):
            if abs(report[i] - report[i + 1]) not in [1, 2, 3]:
                is_safe = False
                break
    else:
        is_safe = False

    if is_safe:
        safe_reports_cnt += 1

ic(safe_reports_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
