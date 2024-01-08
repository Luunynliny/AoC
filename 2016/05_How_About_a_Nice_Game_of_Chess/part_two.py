from hashlib import md5
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    door_id = f.read()

password = [None] * 8
incr = -1

for i in range(8):
    while True:
        incr += 1

        if (
            (
                _hash := md5(str.encode(f"{door_id}{incr}")).hexdigest()
            ).startswith("00000")
            and str.isdigit(_hash[5])
            and (index := int(_hash[5])) < 8
            and password[index] is None
        ):
            password[index] = _hash[6]
            break

password = "".join(password)

ic(password)

exec_time = perf_counter() - timer
ic(exec_time)
