count = 0
position = 50

with open("input.txt") as f:
    for line in f:
        if len(line) == 0:
            break
        if line[0] == "R":
            position = (position + int(line[1:])) % 100
        elif line[0] == "L":
            position = (position - int(line[1:])) % 100
        if position == 0:
            count += 1

print(count)