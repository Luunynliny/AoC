from itertools import count
from math import sqrt
from time import perf_counter

from icecream import ic

timer = perf_counter()


def divisors(n):
    divs = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])

    return set(divs)


house_number = None

for c in count(1):
    if (sum(divisors(c)) * 10) >= 29_000_000:
        house_number = c
        break

ic(house_number)

exec_time = perf_counter() - timer
ic(exec_time)
