count = 0
position = 50

with open("input.txt") as f:
    for line in f:
        if len(line) == 0:
            break
        if line[0] == "R":
            position += int(line[1:])
            while position > 99:
                position -= 100
                count += 1
        elif line[0] == "L":
            # 0 -> 99 doesn't increment count
            # but ending on 0 does increment count
            amount = int(line[1:])
            if (position == 0) and (position - amount) < 0:
                count -= 1
            position -= amount
            while position < 0:
                position += 100
                count += 1
            if position == 0:
                count += 1

print(count)