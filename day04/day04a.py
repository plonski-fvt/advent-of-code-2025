
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


with open("input.txt") as f:
    lines = f.readlines()

rows = len(lines)
# -1 to eliminate the newlines
cols = len(lines[0]) - 1
sums: list[list[int]] = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if lines[i][j] != "@":
            continue
        for a, b in neighbors:
            sample_i = i + a
            sample_j = j + b
            if (sample_i < 0) or (sample_j < 0) or (sample_i) >= rows or (sample_j) >= cols:
                continue
            sums[sample_i][sample_j] += 1

result = 0

print(sums)

for i in range(rows):
    for j in range(cols):
        if (lines[i][j] == "@") and (sums[i][j] < 4):
            result += 1

print(result)