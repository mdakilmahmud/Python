num_list = [2, 4, 3, 77, 32, 5, 12, 35, 68, 50, 100]
odd_numbers = 0
even_numbers = 0
odd_index_sum = 0
even_index_sum = 0
for index, i in enumerate(num_list):
    if i % 2 == 0: 
        even_numbers += 1
        even_index_sum += index
    else:  
        odd_numbers += 1
        odd_index_sum += index
print(f'Odd numbers: {odd_numbers}')
print(f'Even numbers: {even_numbers}')
print(f'Sum of indices of odd numbers: {odd_index_sum}')
print(f'Sum of indices of even numbers: {even_index_sum}')