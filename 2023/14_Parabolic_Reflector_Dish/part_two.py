from hashlib import sha1
from time import perf_counter

import numpy as np
from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()


with open(puzzle) as f:
    plateform = []

    for line in f.read().splitlines():
        plateform.append(list(line))

    plateform = np.array(plateform)


def get_load(arr, loads):
    return sum(
        [np.sum(loads[np.argwhere(row == "O").flatten()]) for row in arr]
    )


plateform = np.rot90(plateform, 1)

cache_hash = []
cache_p = []
duplicate_idx = None

N_CYCLE = 1_000_000_000

for n in range(N_CYCLE):
    for d in range(4):
        for row in plateform:
            head = 0
            tail = 0

            for i, c in enumerate(row):
                if c == "#":
                    if i != 0:
                        row[head:tail] = np.sort(row[head:tail])[::-1]

                    head = i + 1
                    tail = i + 1
                    continue

                tail += 1

                if i == len(row) - 1 and tail != head:
                    row[head : tail + 1] = np.sort(row[head : tail + 1])[::-1]

        plateform = np.rot90(plateform, -1)

    _hash = sha1(np.ascontiguousarray(plateform)).hexdigest()

    if _hash in cache_hash:
        duplicate_idx = (cache_hash.index(_hash), n)
        break

    cache_hash.append(_hash)
    cache_p.append(plateform.copy())

period_len = duplicate_idx[1] - duplicate_idx[0]
end_cycle_id = (N_CYCLE - duplicate_idx[0]) % period_len + duplicate_idx[0] - 1

p = cache_p[end_cycle_id]
loads = np.arange(len(plateform), 0, -1)

total_load = get_load(p, loads)

ic(total_load)

exec_time = perf_counter() - timer
ic(exec_time)
