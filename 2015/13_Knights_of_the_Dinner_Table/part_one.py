from collections import defaultdict
from itertools import permutations
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

seating = defaultdict(dict)

with open(puzzle) as f:
    for line in f.read().splitlines():
        name, _, sign, amount, *_, neighbor = line.split()

        sign = 1 if sign == "gain" else -1
        amount = int(amount) * sign

        seating[name][neighbor[:-1]] = amount

    seating.default_factory = None

guests = list(seating.keys())
max_happiness = 0

for p in permutations(guests[1:]):
    p = (guests[0],) + p
    happiness = 0

    max_happiness = max(
        max_happiness,
        sum(
            seating[p[i - 1]][g] + seating[p[(i + 1) % len(guests)]][g]
            for i, g in enumerate(p)
        ),
    )

ic(max_happiness)

exec_time = perf_counter() - timer
ic(exec_time)
