import re

example = "./example.txt"
puzzle = "./puzzle_input.txt"

with open(puzzle) as f:
    lines = f.read().splitlines()

game_id_sum = 0

cube_color_limit = {"red": 12, "green": 13, "blue": 14}

for game in lines:
    game_split = re.split(r":|,|;", game)

    is_game_possible = True

    for cube_subset in game_split[1:]:
        amount, color = cube_subset.split()

        if int(amount) > cube_color_limit[color]:
            is_game_possible = False
            break

    if not is_game_possible:
        continue

    game_id = game_split[0].split()[-1]
    game_id_sum += int(game_id)

print(game_id_sum)
