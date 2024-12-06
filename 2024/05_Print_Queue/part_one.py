from os import path
from time import perf_counter
from collections import defaultdict

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()
    sep = lines.index("\n")

    rules_to_parse, updates_to_parse = lines[:sep], lines[sep+1:]

    rules = defaultdict(list)
    for r in rules_to_parse:
        a, b = r.strip().split("|")
        rules[int(a)].append(int(b))

    updates = [list(map(int, u.strip().split(","))) for u in updates_to_parse]

middle_page_number_sum = 0

for update in updates:
    pages_cnt = len(update)
    is_rule_error = False

    for i in range(pages_cnt):
        page = update[i]

        if any(page_after not in rules[page] for page_after in update[i+1:]):
            is_rule_error = True
            break

    if not is_rule_error:
        middle_page_number_sum += update[pages_cnt//2]

ic(middle_page_number_sum)

exec_time = perf_counter() - timer
ic(exec_time)
