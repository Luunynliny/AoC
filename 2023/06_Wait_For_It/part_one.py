from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

with open(puzzle) as f:
    lines = f.readlines()

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

ways_product = 1

for i, t in enumerate(times):
    win_count = 0

    for d in ((t - h) * h for h in range(t + 1)):
        if d > distances[i]:
            win_count += 1

    ways_product *= win_count

ic(ways_product)
