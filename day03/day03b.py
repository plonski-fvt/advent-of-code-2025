sum = 0

def find_highest_number(digits: list[int], number_power: int):
    # get everything tied for max that can be the highest
    best_digit = 0
    best_index = 0
    for index, value in enumerate(digits[0:len(digits) - number_power]):
        if value > best_digit:
            best_digit = value
            best_index = index

    if number_power == 0:
        return best_digit

    candidate_number = best_digit * 10 ** number_power + find_highest_number(digits[best_index+1:], number_power - 1)
    return candidate_number
        
with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        digits = [int(c) for c in l if c.isdigit()]
        best_num = find_highest_number(digits, 11)
        print(best_num)
        sum += best_num

print(sum)
