from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

with open(puzzle) as f:
    lines = f.readlines()

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

wins_count = 0

for d in ((time - h) * h for h in range(time + 1)):
    if d > distance:
        wins_count += 1

ic(wins_count)
