from hashlib import md5
from itertools import count
from time import perf_counter

from icecream import ic

puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()

for c in count():
    h = md5(f"{line}{c}".encode()).hexdigest()

    if h[:5] == "00000":
        ic(c)
        break

exec_time = perf_counter() - timer
ic(exec_time)
