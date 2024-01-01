from itertools import count
from time import perf_counter

from icecream import ic

timer = perf_counter()

house_number = None

for c in count(1):
    if 11 * sum([c // n for n in range(1, 51) if c % n == 0]) >= 29_000_000:
        house_number = c
        break

ic(house_number)

exec_time = perf_counter() - timer
ic(exec_time)
