
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

starting_col = lines[0].find("S")

beams: list[set[int]] = [set()]
beams[0].add(starting_col)

num_splits = 0

for row in range(len(lines) - 1):
    beams_in_next_row = set()
    for col in beams[row]:
        if lines[row + 1][col] == "^":
            num_splits += 1
            beams_in_next_row.add(col - 1)
            beams_in_next_row.add(col + 1)
        else:
            beams_in_next_row.add(col)
    beams.append(beams_in_next_row)

print(num_splits)
