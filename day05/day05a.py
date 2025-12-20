import re

pairs: list[tuple[int, int]] = []
vals: list[int] = []

with open("input.txt") as f:
    for line in f.readlines():
        match = re.match(r"(\d+)-(\d+)", line)
        if match is not None:
            pairs.append((int(match.groups()[0]), int(match.groups()[1])))
        elif len(line.strip()) > 0:
            vals.append(int(line.strip()))

print(len(vals))

sum = 0
for val in vals:
    found = False
    for pair in pairs:
        if pair[0] <= val and val <= pair[1]:
            found = True
            break
    if found:
        sum += 1

print(sum)