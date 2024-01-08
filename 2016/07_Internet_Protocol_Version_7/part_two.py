import re
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example_two.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    ips = f.read().splitlines()


def is_pattern(s, hs):
    def regex(text):
        return re.findall(r"(?=([a-z])([a-z])\1)", text)

    matches = regex(s)

    if len(matches) == 0:
        return False

    is_ssl_supported = False

    for m in matches:
        if m[0] != m[1]:
            for h in hs:
                if (m[1], m[0]) in regex(h):
                    is_ssl_supported = True
                    break

            if is_ssl_supported:
                break

    return is_ssl_supported


ssl_supported_ip_cnt = 0

for ip in ips:
    ip_split = re.split("\\[|\\]", ip)

    supernets = ip_split[0::2]
    hypernets = ip_split[1::2]

    for s in supernets:
        if is_pattern(s, hypernets):
            ssl_supported_ip_cnt += 1
            break

ic(ssl_supported_ip_cnt)

exec_time = perf_counter() - timer
ic(exec_time)
