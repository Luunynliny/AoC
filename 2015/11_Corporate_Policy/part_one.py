import re
from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    line = f.read()


def is_conform(s):
    for g in [
        "abc",
        "bcd",
        "cde",
        "def",
        "efg",
        "fgh",
        "ghi",
        "hij",
        "ijk",
        "jkl",
        "klm",
        "lmn",
        "mno",
        "nop",
        "opq",
        "pqr",
        "qrs",
        "rst",
        "stu",
        "tuv",
        "uvw",
        "vwx",
        "wxy",
        "xyz",
    ]:
        if g in s:
            break
    else:
        return False

    if ("i" in s) or ("o" in s) or ("l" in s):
        return False

    if len(re.findall(r"(\w)\1", s)) < 2:
        return False

    return True


def incr(s):
    new_chr = chr((ord(s[-1]) - 97 + 1) % 26 + 97)

    return incr(s[:-1]) + "a" if new_chr == "a" else s[:-1] + new_chr


while not is_conform(line):
    line = incr(line)

next_password = "".join(line)

ic(next_password)

exec_time = perf_counter() - timer
ic(exec_time)
