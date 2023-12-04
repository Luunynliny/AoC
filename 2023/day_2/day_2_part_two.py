import re

example = "./example.txt"
puzzle = "./puzzle.txt"

with open(puzzle) as f:
    lines = f.read().splitlines()

game_power_sum = 0

for game in lines:
    game_split = re.split(r":|,|;", game)

    cube_color_max = {"red": 0, "green": 0, "blue": 0}

    for cube_subset in game_split[1:]:
        amount, color = cube_subset.split()
        cube_color_max[color] = max(cube_color_max[color], int(amount))

    game_power = (
        cube_color_max["red"]
        * cube_color_max["green"]
        * cube_color_max["blue"]
    )
    game_power_sum += game_power

print(game_power_sum)
