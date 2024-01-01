from functools import lru_cache
from os import path
from time import perf_counter

import numpy as np
from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

booklet = {}

with open(puzzle) as f:
    for line in f.read().splitlines():
        l_split = line.split()

        match len(l_split):
            case 3:
                v, _, k = l_split
                booklet[k] = np.uint16(v) if v.isnumeric() else v
            case 4:
                o, a, _, k = l_split
                booklet[k] = (np.uint16(a) if a.isnumeric() else a, o)
            case 5:
                a, o, b, _, k = l_split
                booklet[k] = (
                    np.uint16(a) if a.isnumeric() else a,
                    np.uint16(b) if b.isnumeric() else b,
                    o,
                )


@lru_cache
def signal(k):
    v = booklet[k]

    if type(v) is np.uint16:
        return v

    if type(v) is str:
        return signal(v)

    if len(v) == 2:
        return ~signal(v[0])

    if len(v) == 3:
        a, b, o = v[0], v[1], v[2]

        if type(a) is not np.uint16:
            a = signal(a)

        if type(b) is not np.uint16:
            b = signal(b)

        match o:
            case "AND":
                return a & b
            case "OR":
                return a | b
            case "LSHIFT":
                return a << b
            case "RSHIFT":
                return a >> b


wire_a = signal("a")

ic(wire_a)

exec_time = perf_counter() - timer
ic(exec_time)
