import re
from itertools import batched
from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    _iter = iter(f.read().splitlines())

    workflows = {}
    part_ratings = []

    for line in _iter:
        if line == "":
            break

        k, *rules, _ = re.split("{|:|,|}", line)
        workflows[k] = {}

        for rule in batched(rules, n=2):
            c, *r = rule
            r = r[0] if r else None

            workflows[k][c] = r

    for line in _iter:
        _, x, _, m, _, a, _, s, _ = re.split("=|,|}", line)
        part_ratings.append((int(x), int(m), int(a), int(s)))


def process(flow, ratings):
    x, m, a, s = ratings

    for cond, act in workflows[flow].items():
        if act is None:
            return cond if cond in ["A", "R"] else process(cond, ratings)

        if eval(cond):
            return act if act in ["A", "R"] else process(act, ratings)


accepted_ratings_sum = sum(
    sum([x, m, a, s])
    for x, m, a, s in part_ratings
    if process("in", (x, m, a, s)) == "A"
)

ic(accepted_ratings_sum)

exec_time = perf_counter() - timer
ic(exec_time)
