from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    names, ids, checksums = [], [], []

    for line in f.read().splitlines():
        names.append(line[:-11].replace("-", ""))
        ids.append(int(line[-10:-7]))
        checksums.append(line[-6:-1])


def decrypt(encoded, shift):
    decoded = ""

    for _chr in encoded:
        if _chr == "-":
            continue

        decoded += chr(97 + ((ord(_chr) - 97 + shift) % 26))

    return decoded


for i in range(len(names)):
    if decrypt(names[i], ids[i]) == "northpoleobjectstorage":
        room_id = ids[i]
        break

ic(room_id)

exec_time = perf_counter() - timer
ic(exec_time)
