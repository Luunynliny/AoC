from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()


with open(puzzle) as f:
    lines = f.read().split(",")


def HASH(_str):
    val = 0

    for c in _str:
        val += ord(c)
        val *= 17
        val %= 256

    return val


hash_sum = sum([HASH(s) for s in lines])

ic(hash_sum)

exec_time = perf_counter() - timer
ic(exec_time)
