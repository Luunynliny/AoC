from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    reindeers = []

    for line in f.read().splitlines():
        l_split = line.split()
        reindeers.append((int(l_split[3]), int(l_split[6]), int(l_split[13])))

t = 2503
max_distance = 0

for speed, fly_drt, rest_drt in reindeers:
    cycle_drt = fly_drt + rest_drt

    nb_cycle = t // cycle_drt
    time_left = t % cycle_drt

    d = speed * (
        (nb_cycle * fly_drt) + (fly_drt if fly_drt < time_left else time_left)
    )

    max_distance = max(max_distance, d)

ic(max_distance)

exec_time = perf_counter() - timer
ic(exec_time)
