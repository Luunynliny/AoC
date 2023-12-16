import re
from time import perf_counter

from icecream import ic

puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    aunts_specs = []

    for line in f.read().splitlines():
        k1, v1, k2, v2, k3, v3 = [s for s in re.split(" |,|:", line)[2:] if s]
        aunts_specs.append({k1: int(v1), k2: int(v2), k3: int(v3)})

ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

real_aunt_number = None

for i, spec in enumerate(aunts_specs):
    is_a_match = True

    for k in spec.keys():
        match k:
            case "cats" | "trees":
                if spec[k] <= ticker_tape[k]:
                    is_a_match = False
                    break
            case "pomeranians" | "goldfish":
                if spec[k] >= ticker_tape[k]:
                    is_a_match = False
                    break
            case _:
                if spec[k] != ticker_tape[k]:
                    is_a_match = False
                    break

    if is_a_match:
        real_aunt_number = i + 1
        break

ic(real_aunt_number)

exec_time = perf_counter() - timer
ic(exec_time)
