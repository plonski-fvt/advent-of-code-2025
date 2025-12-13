import re

total = 0
pattern = r'(\d+)\1+'

with open("input.txt") as f:
    line = f.readline()
    ranges = line.split(",")
    for r in ranges:
        print(r)
        ids = r.split("-")
        for id in range(int(ids[0]), int(ids[1]) + 1):
            match = re.fullmatch(pattern, str(id))
            if match is not None:
                print(match.group(0))
                total += int(match.group(0))

print(total)