from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

def is_report_safe(report, level_removed=False):
    is_safe = True

    if sorted(report) == report or sorted(report, reverse=True) == report:
        for i in range(len(report) - 1):
            if abs(report[i] - report[i + 1]) not in [1, 2, 3]:
                is_safe = False
                break
    else:
        is_safe = False

    if not level_removed and not is_safe:
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)

            if is_report_safe(report_copy, True):
                is_safe = True
                break

    return is_safe

with open(puzzle) as f:
    lines = f.readlines()

safe_reports_cnt = sum([is_report_safe(list(map(int, line.split()))) for line in lines])

ic(safe_reports_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
