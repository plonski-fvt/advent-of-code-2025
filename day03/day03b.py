sum = 0

def find_highest_number(digits: list[int], number_power: int):
    
    # get everything tied for max that can be the highest
    best_digit = 0
    best_indices = []
    for index, value in enumerate(digits[0:len(digits) - number_power]):
        if value > best_digit:
            best_digit = value
            best_indices = [index]
        elif value == best_digit:
            best_indices.append(index)

    if number_power == 0:
        return best_digit

    highest_number = 0
    for index in best_indices:
        candidate_number = best_digit * 10 ** number_power + find_highest_number(digits[index+1:], number_power - 1)
        if candidate_number > highest_number:
            highest_number = candidate_number

    return highest_number
        



with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        digits = [int(c) for c in l if c.isdigit()]
        best_num = find_highest_number(digits, 11)
        print(best_num)
        sum += best_num

print(sum)
