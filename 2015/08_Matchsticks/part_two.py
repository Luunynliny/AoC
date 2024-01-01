from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read().splitlines()

nb_encoded_char = sum(
    [len(s) + s.count('"') + s.count("\\") + 2 for s in lines]
)
nb_literal_char = sum([len(s) for s in lines])

code_memory_diff = nb_encoded_char - nb_literal_char

ic(code_memory_diff)

exec_time = perf_counter() - timer
ic(exec_time)
