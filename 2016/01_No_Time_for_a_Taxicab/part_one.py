from enum import Enum
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


class Facing(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3


facing = Facing.NORTH
pos_x, pos_y = 0, 0

for rot, n in instructions:
    match facing:
        case Facing.NORTH:
            facing = Facing.EAST if rot == "R" else Facing.WEST
            pos_y += n if rot == "R" else -n
        case Facing.WEST:
            facing = Facing.NORTH if rot == "R" else Facing.SOUTH
            pos_x += n if rot == "R" else -n
        case Facing.SOUTH:
            facing = Facing.WEST if rot == "R" else Facing.EAST
            pos_y += -n if rot == "R" else n
        case Facing.EAST:
            facing = Facing.SOUTH if rot == "R" else Facing.NORTH
            pos_x += -n if rot == "R" else n

blocks_away_cnt = abs(pos_x) + abs(pos_y)

ic(blocks_away_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
