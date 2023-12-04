from icecream import ic

example = "./example.txt"
puzzle = "./puzzle.txt"

matrix = []

with open(puzzle) as f:
    for line in f.read().splitlines():
        matrix.append(line)

number_dict = {}
symbol_dict = {}

for i, row in enumerate(matrix):
    number_str = ""
    start_j = 0

    for j, col in enumerate(row):
        c = matrix[i][j]

        if c.isdigit():
            if len(number_str) == 0:
                start_j = j

            number_str += c

            if j < len(row) - 1:
                continue

        elif c != ".":
            if symbol_dict.get(i):
                symbol_dict[i].append(j)
            else:
                symbol_dict[i] = [j]

        if len(number_str) > 0:
            key = f"{start_j}_{start_j + len(number_str) - 1}"
            number = int(number_str)

            if number_dict.get(i):
                number_dict[i][key] = number
            else:
                number_dict[i] = {key: number}

            number_str = ""

ic(number_dict)
ic(symbol_dict)

part_number_sum = 0

for row in [int(r) for r in symbol_dict.keys()]:
    for col in symbol_dict[row]:
        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 and y == 0:
                    continue

                nrow = row + x
                ncol = col + y

                if (
                    nrow < 0
                    or nrow >= len(matrix)
                    or ncol < 0
                    or ncol >= len(matrix[0])
                ):
                    continue

                if not number_dict.get(nrow):
                    continue

                keys = list(number_dict[nrow].keys()).copy()
                for key in keys:
                    s_i, e_i = key.split("_")
                    s_i, e_i = int(s_i), int(e_i)

                    if not (s_i <= ncol <= e_i):
                        continue

                    part_number_sum += number_dict[nrow][key]

                    del number_dict[nrow][key]

ic(part_number_sum)
