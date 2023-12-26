import re
from itertools import cycle
from time import perf_counter

from icecream import ic

example = "./example_one.txt"
puzzle = "./puzzle.txt"

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

node = "AAA"
step_count = 0

for direction in cycle(directions):
    if node == "ZZZ":
        break

    node_index = nodes.index(node)
    next_node = lefts[node_index] if direction == "L" else rights[node_index]

    node = next_node
    step_count += 1

ic(step_count)

exec_time = perf_counter() - timer
ic(exec_time)
