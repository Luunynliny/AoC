from time import perf_counter

from icecream import ic

example = "./example_two.txt"
puzzle = "./puzzle.txt"

timer = perf_counter()

maze = []

with open(puzzle) as f:
    for i, line in enumerate(f.read().splitlines()):
        tiles = list(line)

        if "S" in tiles:
            s_pos = (i, tiles.index("S"))

        maze.append(tiles)

compatibily_dict = {
    "left": ["-", "L", "F"],
    "down": ["|", "L", "J"],
    "right": ["-", "J", "7"],
    "up": ["|", "7", "F"],
}

sx, sy = s_pos
w, h = len(maze), len(maze[0])

# https://stackoverflow.com/a/38157488
s_neighbors = [
    (sx + a[0], sy + a[1])
    for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if ((0 <= sx + a[0] < w) and (0 <= sy + a[1] < h))
]

for x, y in s_neighbors:
    if (n := maze[x][y]) == ".":
        continue

    match sx - x, sy - y:
        case -1, 0:
            dir_ = "down"
        case 1, 0:
            dir_ = "up"
        case 0, -1:
            dir_ = "right"
        case 0, 1:
            dir_ = "left"

    if n in compatibily_dict[dir_]:
        pos = (x, y)
        break


def next_pos(pos, dir_, tile=None):
    x, y = pos

    match maze[x][y] if not tile else tile:
        case "|":
            x += 1 if dir_ == "down" else -1
        case "-":
            y += 1 if dir_ == "right" else -1
        case "L":
            return (
                next_pos(pos, "right", "-")
                if dir_ == "down"
                else next_pos(pos, "up", "|")
            )
        case "J":
            return (
                next_pos(pos, "left", "-")
                if dir_ == "down"
                else next_pos(pos, "up", "|")
            )
        case "7":
            return (
                next_pos(pos, "left", "-")
                if dir_ == "up"
                else next_pos(pos, "down", "|")
            )
        case "F":
            return (
                next_pos(pos, "right", "-")
                if dir_ == "up"
                else next_pos(pos, "down", "|")
            )

    return (x, y), dir_


loop = [s_pos]

while pos != s_pos:
    loop.append(pos)
    pos, dir_ = next_pos(pos, dir_)

nb_points = len(loop)

area = abs(
    sum(
        [
            (loop[i][0] * loop[(i + 1) % nb_points][1])
            - (loop[(i + 1) % nb_points][0] * loop[i][1])
            for i in range(nb_points)
        ]
    )
    // 2
)

enclosed_tile_count = area - (nb_points // 2) + 1

ic(enclosed_tile_count)

exec_time = perf_counter() - timer
ic(exec_time)
