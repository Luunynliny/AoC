import re
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_one.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    ips = f.read().splitlines()


def is_pattern(text):
    matches = re.findall(r"([a-z])([a-z])\2\1", text)

    if len(matches) == 0:
        return False

    is_different = False

    for m in matches:
        if m[0] != m[1]:
            is_different = True
            break

    return is_different


tls_supported_ip_cnt = 0

for ip in ips:
    ip_split = re.split("\\[|\\]", ip)

    is_tls_supported = False

    for i, s in enumerate(ip_split):
        if i % 2 == 0:
            is_tls_supported = is_tls_supported | is_pattern(s)
        else:
            if is_pattern(s):
                is_tls_supported = False
                break

    if is_tls_supported:
        tls_supported_ip_cnt += 1

ic(tls_supported_ip_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
