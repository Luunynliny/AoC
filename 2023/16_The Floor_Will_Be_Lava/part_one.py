from enum import Enum
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    grid = np.array([list(l) for l in f.read().splitlines()])


class Way(Enum):
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    UP = 4


DELTA = {
    ".": {
        Way.RIGHT: (0, 1, Way.RIGHT),
        Way.LEFT: (0, -1, Way.LEFT),
        Way.UP: (-1, 0, Way.UP),
        Way.DOWN: (1, 0, Way.DOWN),
    },
    "\\": {
        Way.LEFT: (-1, 0, Way.UP),
        Way.DOWN: (0, 1, Way.RIGHT),
        Way.RIGHT: (1, 0, Way.DOWN),
        Way.UP: (0, -1, Way.LEFT),
    },
    "/": {
        Way.LEFT: (1, 0, Way.DOWN),
        Way.DOWN: (0, -1, Way.LEFT),
        Way.RIGHT: (-1, 0, Way.UP),
        Way.UP: (0, 1, Way.RIGHT),
    },
}

light_cache = []


def diffuse_light(grid, ij, way):
    i, j = ij
    max_i, max_j = grid.shape

    while (
        0 <= i < max_i
        and 0 <= j < max_j
        and (tile_specs := (i, j, way)) not in light_cache
    ):
        light_cache.append(tile_specs)

        match tile := grid[i, j]:
            case "|":
                if way == Way.LEFT or way == Way.RIGHT:
                    diffuse_light(grid, (i - 1, j), Way.UP)
                    diffuse_light(grid, (i + 1, j), Way.DOWN)
                    break

                tile = "."
            case "-":
                if way == Way.UP or way == Way.DOWN:
                    diffuse_light(grid, (i, j - 1), Way.LEFT)
                    diffuse_light(grid, (i, j + 1), Way.RIGHT)
                    break

                tile = "."

        di, dj, nw = DELTA[tile][way]

        i += di
        j += dj
        way = nw


diffuse_light(grid, ij=(0, 0), way=Way.RIGHT)

energized_tile_cnt = len(set([(i, j) for i, j, _ in light_cache]))

ic(energized_tile_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
