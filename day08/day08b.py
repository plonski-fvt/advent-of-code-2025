import math

coords: list[tuple[int, int, int]] = []

with open("input.txt") as f:
    for line in f.readlines():
        coords_strings = line.split(",")
        coords.append(
            (int(coords_strings[0]), int(coords_strings[1]), int(coords_strings[2]))
        )

distances_i_j: list[tuple[float, int, int]] = []

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        distance = math.sqrt(
            (coords[i][0] - coords[j][0]) ** 2 +
            (coords[i][1] - coords[j][1]) ** 2 +
            (coords[i][2] - coords[j][2]) ** 2
        )
        distances_i_j.append((distance, i, j))

distances_i_j.sort()

circuit_indices = list(range(len(coords))) # start out with n circuits
circuit_index_exists = set(circuit_indices)

for i in range(1000000):
    distance, a, b = distances_i_j[i]
    a_circuit = circuit_indices[a]
    b_circuit = circuit_indices[b]
    if a_circuit == b_circuit:
        continue
    circuit_indices = [a_circuit if x == b_circuit else x for x in circuit_indices]
    circuit_index_exists.discard(b_circuit)
    if len(circuit_index_exists) == 1:
        print(f"answer: {coords[a][0] * coords[b][0]}")
        break


count_circuit_index: list[tuple[int, int]] = []

for i in range(len(coords)):
    count = sum(i == x for x in circuit_indices)
    count_circuit_index.append((count, i))

count_circuit_index.sort(reverse=True)

print(count_circuit_index)