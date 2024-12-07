num=int(input('Enter a number: '))
num_reverse=0
num_str=str(num)
for digit in str(num)[::-1]:
      num_reverse= num_reverse * 10 + int(digit)
print(num_reverse)