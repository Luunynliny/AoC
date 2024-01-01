from ast import literal_eval
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    lines = f.read().splitlines()

nb_code_char = sum([len(s) for s in lines])
nb_memory_char = sum([len(literal_eval(s)) for s in lines])

code_memory_diff = nb_code_char - nb_memory_char

ic(code_memory_diff)

exec_time = perf_counter() - timer
ic(exec_time)
