from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

with open(puzzle) as f:
    lines = f.read()

seeds_input, *maps_input = lines.split("\n\n")
seeds = list(map(int, seeds_input.split()[1:]))

for mi in maps_input:
    next_seeds = seeds.copy()

    for data in mi.split("\n")[1:]:
        dest, src, r = tuple(map(int, data.split()))

        for i in range(len(seeds)):
            seed = seeds[i]

            if src <= seed <= src + (r - 1):
                next_seeds[i] = dest + (seed - src)

    seeds = next_seeds

ic(min(seeds))
