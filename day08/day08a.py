from scipy.spatial import KDTree

coords: list[tuple[int, int, int]] = []

with open("input.txt") as f:
    for line in f.readlines():
        coords_strings = line.split(",")
        coords.append(
            (int(coords_strings[0]), int(coords_strings[1]), int(coords_strings[2]))
        )

box_tree = KDTree(coords)

shortest_distances = []
has_edge: set[tuple[int, int]] = set()

# TODO: this doesn't work because what if e.g. the first 10 closest overall distances involve the same box???

for i, coord in enumerate(coords):
    d, j = box_tree.query(coord, 2)
    if (i, j[1]) in has_edge or (j[1], i) in has_edge:
        continue
    shortest_distances.append(
        (d[1], i, j[1])
    )
    has_edge.add((i, j[1]))

shortest_distances.sort()

circuit_indices = list(range(len(coords))) # start out with n circuits

for i in range(1000):
    distance, a, b = shortest_distances[i]
    a_circuit = circuit_indices[a]
    b_circuit = circuit_indices[b]
    circuit_indices = [a_circuit if x == b_circuit else x for x in circuit_indices]


count_circuit_index: list[tuple[int, int]] = []

for i in range(len(coords)):
    count = sum(i == x for x in circuit_indices)
    count_circuit_index.append(count, i)

count_circuit_index.sort()

print(count_circuit_index)

print(count_circuit_index[0][0] * count_circuit_index[1][0] * count_circuit_index[2][0])