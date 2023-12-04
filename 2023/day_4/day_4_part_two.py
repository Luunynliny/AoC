from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

with open(puzzle) as f:
    lines = f.read().splitlines()

cards_count = [1] * len(lines)

for i, line in enumerate(lines):
    l_split = line.split("|")

    winning_numbers = set(l_split[0].split()[2:])
    numbers = set(l_split[1].split())

    matches = winning_numbers & numbers

    for j in range(0, len(matches)):
        if i + j + 1 >= len(lines):
            break

        cards_count[i + j + 1] += 1 * cards_count[i]

ic(cards_count)
ic(sum(cards_count))
