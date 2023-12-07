from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read().splitlines()

points_total = 0

for line in lines:
    l_split = line.split("|")

    winning_numbers = set(l_split[0].split()[2:])
    numbers = set(l_split[1].split())

    matches = winning_numbers & numbers

    if len(matches) > 0:
        points_total += 2 ** (len(matches) - 1)

ic(points_total)

exec_time = perf_counter() - timer
ic(exec_time)
