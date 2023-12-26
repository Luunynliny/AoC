from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    instructions = []

    for line in f.read().splitlines():
        _dir, steps, _ = line.split()
        instructions.append((_dir, int(steps)))

corners = [(0, 0)]

for _dir, steps in instructions[::-1]:
    i, j = corners[-1]

    match _dir:
        case "L":
            j -= steps
        case "D":
            i += steps
        case "R":
            j += steps
        case "U":
            i -= steps

    corners.append((i, j))

nb_points = len(corners)

perimeter = sum(
    [
        abs(corners[i][0] - corners[(i + 1) % nb_points][0])
        + abs(corners[i][1] - corners[(i + 1) % nb_points][1])
        for i in range(nb_points)
    ]
)

shoelace = abs(
    sum(
        [
            (corners[i][0] * corners[(i + 1) % nb_points][1])
            - (corners[(i + 1) % nb_points][0] * corners[i][1])
            for i in range(nb_points)
        ]
    )
    // 2
)

lava_capacity = perimeter // 2 + 1 + shoelace

ic(lava_capacity)

exec_time = perf_counter() - timer
ic(exec_time)
