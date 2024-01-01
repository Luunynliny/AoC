from functools import cache
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

springs_lst = []
groups_lst = []

with open(puzzle) as f:
    for line in f.read().splitlines():
        sprg, grp = line.split()

        sprg = "?".join((sprg,) * 5)
        grp = [int(g) for g in grp.split(",")] * 5

        springs_lst.append(sprg)
        groups_lst.append(grp)


@cache
def arrangement_cnt(springs, groups):
    if not groups:
        return 1 if "#" not in springs else 0

    cnt = 0

    for pos in range(
        len(springs) - sum(groups[1:]) + len(groups[1:]) - groups[0] + 1
    ):
        arrangements = "." * pos + "#" * groups[0] + "."

        for spring, arrangement in zip(springs, arrangements):
            if spring != arrangement and spring != "?":
                break
        else:
            cnt += arrangement_cnt(springs[len(arrangements) :], groups[1:])

    return cnt


arrangement_cnt_sum = sum(
    [
        arrangement_cnt(tuple(springs_lst[i]), tuple(groups_lst[i]))
        for i in range(len(springs_lst))
    ]
)

ic(arrangement_cnt_sum)

exec_time = perf_counter() - timer
ic(exec_time)
