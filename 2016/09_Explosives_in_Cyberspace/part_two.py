from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    _file = f.read()


def decompress_size(text):
    size = 0
    i = 0

    while i < len(text):
        if str.isalpha(text[i]):
            size += 1
            i += 1
        else:
            j = i + 1
            while text[j] != ")":
                j += 1

            marker = text[i + 1 : j]
            l, t = list(map(int, marker.split("x")))

            i = j + l + 1
            size += t * decompress_size(text[j + 1 : i])

    return size


decompressed_length = decompress_size(_file)
ic(decompressed_length)

exec_time = perf_counter() - timer
ic(exec_time)
