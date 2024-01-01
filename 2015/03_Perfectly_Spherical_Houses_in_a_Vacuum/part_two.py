from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()

loc_unique = []

for directions in (line[::2], line[1::2]):
    x, y = 0, 0

    for direction in directions:
        match direction:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1

        loc = (x, y)

        if loc not in loc_unique:
            loc_unique.append(loc)

house_count = len(loc_unique)

ic(house_count)

exec_time = perf_counter() - timer
ic(exec_time)
