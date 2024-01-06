from enum import Enum
from math import copysign
from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    instructions = []

    for step in f.read().split(", "):
        rot, n = step[0], step[1:]

        instructions.append((rot, int(n)))


def sign(x):
    return int(copysign(1, x))


class Facing(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3


facing = Facing.NORTH
pos = (0, 0)

visited = {pos}
found_twice = False

for rot, n in instructions:
    next_x, next_y = 0, 0

    match facing:
        case Facing.NORTH:
            facing = Facing.EAST if rot == "R" else Facing.WEST
            next_y = n if rot == "R" else -n
        case Facing.WEST:
            facing = Facing.NORTH if rot == "R" else Facing.SOUTH
            next_x = n if rot == "R" else -n
        case Facing.SOUTH:
            facing = Facing.WEST if rot == "R" else Facing.EAST
            next_y = -n if rot == "R" else n
        case Facing.EAST:
            facing = Facing.SOUTH if rot == "R" else Facing.NORTH
            next_x = -n if rot == "R" else n

    for dx, dy in [
        (0, sign(next_y)) if next_x == 0 else (sign(next_x), 0)
        for _ in range(1, abs(next_y) + 1 if next_x == 0 else abs(next_x) + 1)
    ]:
        pos = (pos[0] + dx, pos[1] + dy)

        if pos in visited:
            print("fouds")
            found_twice = True
            break

        visited.add(pos)

    if found_twice:
        break

blocks_away_cnt = sum(map(abs, pos))

ic(blocks_away_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
