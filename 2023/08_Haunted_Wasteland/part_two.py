import re
from itertools import cycle
from math import lcm
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_two.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.readlines()

directions = [d for d in lines[0][:-1]]

nodes = []
lefts = []
rights = []

for line in lines[2:]:
    node, left, right = re.findall(r"\w+", line)

    if node + left + right == node * 3:
        continue

    nodes.append(node)
    lefts.append(left)
    rights.append(right)

start_nodes = [n for n in nodes if n[2] == "A"]
cycle_lengths = []

for node in start_nodes:
    cycle_length = 0

    for direction in cycle(directions):
        if node[2] == "Z":
            break

        node_index = nodes.index(node)
        next_node = (
            lefts[node_index] if direction == "L" else rights[node_index]
        )

        node = next_node
        cycle_length += 1

    cycle_lengths.append(cycle_length)

step_count = lcm(*cycle_lengths)

ic(step_count)

exec_time = perf_counter() - timer
ic(exec_time)
