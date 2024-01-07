from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    sequences = []

    for line in f.read().splitlines():
        sequences.append(list(line))

KEYPAD = [
    "__1__",
    "_234_",
    "56789",
    "_ABC_",
    "__D__",
]

button = "5"
i_pos, j_pos = 2, 0

bathroom_code = ""

for sequence in sequences:
    for move in sequence:
        if move in "UD":
            new_i_pos = i_pos - 1 if move == "U" else i_pos + 1

            if new_i_pos < 0 or new_i_pos > 4:
                continue

            if (next_button := KEYPAD[new_i_pos][j_pos]) == "_":
                continue

            button = next_button
            i_pos = new_i_pos
        else:
            new_j_pos = j_pos - 1 if move == "L" else j_pos + 1

            if new_j_pos < 0 or new_j_pos > 4:
                continue

            if (next_button := KEYPAD[i_pos][new_j_pos]) == "_":
                continue

            button = next_button
            j_pos = new_j_pos

    bathroom_code += button

ic(bathroom_code)

exec_time = perf_counter() - timer
ic(exec_time)
