
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

starting_col = lines[0].find("S")

beams: list[dict[int, int]] = [{starting_col : 1}]

for row in range(len(lines) - 1):
    beams_in_next_row = {}
    for col, number in beams[row].items():
        if lines[row + 1][col] == "^":
            beams_in_next_row[col - 1] = beams_in_next_row.setdefault(col - 1, 0) + number
            beams_in_next_row[col + 1] = beams_in_next_row.setdefault(col + 1, 0) + number
        else:
            beams_in_next_row[col] = beams_in_next_row.setdefault(col, 0) + number
    print(beams_in_next_row)
    beams.append(beams_in_next_row)

print(sum(beams[-1].values()))
