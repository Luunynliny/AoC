from os import path
from time import perf_counter

from icecream import ic

puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

with open(puzzle) as f:
    operations = []

    for line in f.read().splitlines():
        l_split = line.split(" ")

        match len(l_split):
            case 2:
                a, b = l_split[1].split("x")
                operations.append((l_split[0], int(a), int(b)))
            case 5:
                operations.append(
                    (l_split[1], int(l_split[2][2:]), int(l_split[4]))
                )

W, T = 50, 6
grid = [["." for _ in range(W)] for _ in range(T)]

for cmd, a, b in operations:
    match cmd:
        case "rect":
            for i in range(b):
                for j in range(a):
                    grid[i][j] = "#"
        case "row":
            # https://stackoverflow.com/a/61287028
            grid[a] = grid[a][-b:] + grid[a][:-b]
        case "column":
            col = [grid[i][a] for i in range(T)]
            shift = col[-b:] + col[:-b]

            for i in range(T):
                grid[i][a] = shift[i]

for j in range(0, W, 5):
    chr_lines = []

    for i in range(T):
        chr_lines.append("".join(grid[i][j : (j + 4)]))

    character = "\n".join(chr_lines).replace(".", " ")
    ic(character)

exec_time = perf_counter() - timer
ic(exec_time)
