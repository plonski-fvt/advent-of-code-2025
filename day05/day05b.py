import re

pairs: list[tuple[int, int]] = []

def test_pair_intersection(pair_a: tuple[int, int], pair_b: tuple[int, int]):
    disjoint = (pair_a[1] < pair_b[0]) or (pair_a[0] > pair_b[1])
    return not disjoint

def merge_pairs(pair_a: tuple[int, int], pair_b: tuple[int, int]):
    return (min(pair_a[0], pair_b[0]), max(pair_a[1], pair_b[1]))

with open("input.txt") as f:
    for line in f.readlines():
        match = re.match(r"(\d+)-(\d+)", line)
        if match is not None:
            pairs.append((int(match.groups()[0]), int(match.groups()[1])))
        else:
            break

print(len(pairs))

for iii in range(len(pairs)):
    found_overlap = False
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if test_pair_intersection(pairs[i], pairs[j]):
                pairs[i] = merge_pairs(pairs[i], pairs[j])
                del pairs[j]
                found_overlap = True
                break
        if found_overlap:
            break
    if not found_overlap:
        break

print(len(pairs))

sum = 0
for pair in pairs:
    sum += 1 + pair[1] - pair[0]

print(sum)
        