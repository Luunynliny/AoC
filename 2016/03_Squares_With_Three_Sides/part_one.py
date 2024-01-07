from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    triangles = [
        sorted(list(map(int, l.split()))) for l in f.read().splitlines()
    ]

possible_triangle_cnt = sum([a + b > c for a, b, c in triangles])

ic(possible_triangle_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
