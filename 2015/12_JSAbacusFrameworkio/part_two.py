import json
import re
from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()


def hook(obj):
    return {} if "red" in obj.values() else obj


without_red = str(json.loads(line, object_hook=hook))

number_sum_without_red = sum(
    [int(n) for n in re.findall(r"-?(?:\d+)+", without_red)]
)

ic(number_sum_without_red)

exec_time = perf_counter() - timer
ic(exec_time)
