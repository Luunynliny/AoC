from collections import Counter
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_one.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    names, ids, checksums = [], [], []

    for line in f.read().splitlines():
        names.append(line[:-11].replace("-", ""))
        ids.append(int(line[-10:-7]))
        checksums.append(line[-6:-1])

real_room_ids_sum = sum(
    [
        ids[i]
        if checksums[i]
        == "".join(dict(Counter(sorted(names[i])).most_common(5)).keys())
        else 0
        for i in range(len(names))
    ]
)

ic(real_room_ids_sum)

exec_time = perf_counter() - timer
ic(exec_time)
