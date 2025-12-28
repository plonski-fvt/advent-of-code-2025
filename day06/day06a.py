from functools import reduce

cols = []
operators = []

with open("input.txt") as f:
    for line in f.readlines():
        if len(cols) == 0:
            num_cols = len(line.split())
            cols = [[] for _ in range(num_cols)]
            operators = [""] * num_cols
        for i, val in enumerate(line.split()):
            try:
                int_val = int(val)
                cols[i].append(int_val)
            except:
                operators[i] = val

# print(cols)
print(operators)

sum = 0

for i, operator in enumerate(operators):
    match operator:
        case "+":
            result = reduce(lambda a, b: a + b, cols[i])
        case "*":
            result = reduce(lambda a, b: a * b, cols[i])
    sum += result

print(sum)

