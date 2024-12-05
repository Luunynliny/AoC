from os import path
from time import perf_counter
import re

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_two.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = "".join(f.readlines())

do_split = line.split("do()")

dos = ""
for do in do_split:
    if "don't()" in do:
        do = do.split("don't()")[0]

    dos += do

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", dos)

result = 0
for mult in matches:
    a, b = re.findall(r"(\d+)", mult)
    result += int(a) * int(b)

ic(result)

exec_time = perf_counter() - timer
ic(exec_time)
