num=[22,42,12,6,0,44,346,23,9,3]
numbers = list(map(int,num))
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(f"Maximum: {max_num}")