n = int(input("N = "))
numbers = list(map(int,input("Numbers: ").split(',')))
if len(numbers) != n:
    print("Error: The number of inputs does not match N.")
else:
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    print(f"Maximum: {max_num}")