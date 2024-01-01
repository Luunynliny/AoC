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

mirror_cache = []


def diffuse_light(ij, way, reset_mirror_cache=False):
    if reset_mirror_cache:
        mirror_cache.clear()

    i, j = ij
    max_i, max_j = grid.shape

    tiles = []

    while 0 <= i < max_i and 0 <= j < max_j:
        if (tile := grid[i, j]) != ".":
            if (tile_specs := (i, j, way)) in mirror_cache:
                return tiles

            mirror_cache.append(tile_specs)

        tiles.append((i, j))

        match tile:
            case "|":
                if way == Way.LEFT or way == Way.RIGHT:
                    tiles.extend(diffuse_light((i - 1, j), Way.UP))
                    tiles.extend(diffuse_light((i + 1, j), Way.DOWN))

                    return tiles

                tile = "."
            case "-":
                if way == Way.UP or way == Way.DOWN:
                    tiles.extend(diffuse_light((i, j - 1), Way.LEFT))
                    tiles.extend(diffuse_light((i, j + 1), Way.RIGHT))

                    return tiles

                tile = "."

        di, dj, nw = DELTA[tile][way]

        i += di
        j += dj
        way = nw

    return tiles


beams_start_configs = (
    [(0, i, Way.DOWN) for i in range(grid.shape[1])]
    + [(i, 0, Way.RIGHT) for i in range(grid.shape[0])]
    + [(grid.shape[0] - 1, i, Way.UP) for i in range(grid.shape[1])]
    + [(i, grid.shape[1] - 1, Way.LEFT) for i in range(grid.shape[0])]
)

energized_tile_max = max(
    [
        len(set(diffuse_light(ij=(i, j), way=w, reset_mirror_cache=True)))
        for i, j, w in beams_start_configs
    ]
)

ic(energized_tile_max)

exec_time = perf_counter() - timer
ic(exec_time)
