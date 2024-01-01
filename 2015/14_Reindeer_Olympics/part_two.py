from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    reindeers = []

    for line in f.read().splitlines():
        l_split = line.split()
        reindeers.append((int(l_split[3]), int(l_split[6]), int(l_split[13])))


reindeer_score = [0] * len(reindeers)

for t in range(1, 2503):
    distances = []

    for speed, fly_drt, rest_drt in reindeers:
        cycle_drt = fly_drt + rest_drt

        nb_cycle = t // cycle_drt
        time_left = t % cycle_drt

        d = speed * (
            (nb_cycle * fly_drt)
            + (fly_drt if fly_drt < time_left else time_left)
        )
        distances.append(d)

    for i in np.argwhere(distances == np.max(distances)).flatten():
        reindeer_score[i] += 1

max_points = max(reindeer_score)

ic(max_points)

exec_time = perf_counter() - timer
ic(exec_time)
