from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    triangles = [list(map(int, l.split())) for l in f.read().splitlines()]

vertical_triangles = []

for i in range(0, len(triangles), 3):
    vertical_triangles.extend(
        [
            sorted(
                [triangles[i][0], triangles[i + 1][0], triangles[i + 2][0]]
            ),
            sorted(
                [triangles[i][1], triangles[i + 1][1], triangles[i + 2][1]]
            ),
            sorted(
                [triangles[i][2], triangles[i + 1][2], triangles[i + 2][2]]
            ),
        ]
    )

possible_triangle_cnt = sum([a + b > c for a, b, c in vertical_triangles])

ic(possible_triangle_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
