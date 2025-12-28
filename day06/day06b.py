def col_to_number(col):
    col_str = ""
    for char in col:
        col_str = col_str + char
    stripped_col_str = col_str.strip()
    if len(stripped_col_str) == 0:
        return None
    return int(stripped_col_str)

cols = []

with open("input.txt") as f:
    for line in f.readlines():
        if len(cols) == 0:
            num_cols = len(line) - 1 # don't want the newline
            cols = [[] for _ in range(num_cols)]
        for i, val in enumerate(line):
            if i < num_cols:
                cols[i].append(val)

print(cols)

operator = cols[0][-1]
partial_sum = 0
sum = 0

for col in cols:
    if col[-1] in ["+", "*"]:
        sum += partial_sum
        operator = col[-1]
        if operator == "+":
            partial_sum = 0 # additive identity
        else:
            partial_sum = 1 # multiplicative identity
    
    col_as_number = col_to_number(col[:-1])
    if col_as_number is not None:
        if operator == "+":
            partial_sum += col_as_number
        else:
            partial_sum *= col_as_number

sum += partial_sum

print(sum)
