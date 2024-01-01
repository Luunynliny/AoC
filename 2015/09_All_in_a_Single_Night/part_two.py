from itertools import pairwise, permutations
from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

adj_matrix = {}

with open(puzzle) as f:
    for line in f.read().splitlines():
        s, _, d, *_, w = line.split()

        adj_matrix.setdefault(s, dict())[d] = int(w)
        adj_matrix.setdefault(d, dict())[s] = int(w)

longest_route_distance = max(
    [
        sum(adj_matrix[u][v] for u, v in pairwise(p))
        for p in permutations(adj_matrix)
    ]
)

ic(longest_route_distance)

exec_time = perf_counter() - timer
ic(exec_time)
