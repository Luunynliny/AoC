from collections import OrderedDict
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()


with open(puzzle) as f:
    lines = f.read().split(",")


def h_a_s_h(_str):
    val = 0

    for c in _str:
        val += ord(c)
        val *= 17
        val %= 256

    return val


boxes = [OrderedDict() for _ in range(256)]

for instr in lines:
    if "-" in instr:
        lbl = instr[:-1]
        boxe_id = h_a_s_h(lbl)

        if lbl in boxes[boxe_id].keys():
            del boxes[boxe_id][lbl]
    else:
        lbl, fl = instr.split("=")
        boxe_id = h_a_s_h(lbl)

        boxes[boxe_id][lbl] = int(fl)

focusing_power_sum = sum(
    [
        (i + 1) * sum([(j + 1) * fl for j, fl in enumerate(d.values())])
        for i, d in enumerate(boxes)
        if len(d) > 0
    ]
)

ic(focusing_power_sum)

exec_time = perf_counter() - timer
ic(exec_time)
