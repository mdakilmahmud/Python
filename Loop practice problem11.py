N=int(input('Enter the number of inputs(N): '))
total=0
for i in range(N):
      num= float(input(f'Enter number{i+1}: '))
      total+=num 
average=total/N
print(f'Average {N}:{average}')