sum = 0

with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        best_num = 0
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                try:
                    num = 10 * int(l[i]) + int(l[j])
                    if num > best_num:
                        best_num = num
                except:
                    pass
        print(best_num)
        sum += best_num

print(sum)
