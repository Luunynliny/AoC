from time import perf_counter

from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

with open(puzzle) as f:
    instructions = []

    for line in f.read().splitlines():
        *_, color = line.split()

        steps = int(color[2:-2], 16)

        match color[-2]:
            case "0":
                _dir = "R"
            case "1":
                _dir = "D"
            case "2":
                _dir = "L"
            case "3":
                _dir = "U"

        instructions.append((_dir, steps))

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
