# Write a function that takes a number n as input and 
# prints a multiplication table up to n x n.

def multiplication_table():
      num=int(input('Enter a number: '))
      for i in range(1,num+1):
            for j in range(1,num+1):
                  print(f"{i * j}", end=" ")
            print()
multiplication_table()

# Write a function that generates Pascal's Triangle up to n rows.

def pascals_triangle():
      n=int(input('Enter a number: '))
      if n<=0:
            print("Error! Number of Row can't be 0")
      triangle=[]
      for i in range(n):
            row=[1]
            if triangle:
                  last_row=triangle[-1]
                  for j in range(len(last_row)-1):
                        row.append(last_row[j]+last_row[j+1])
                  row.append(1)
            triangle.append(row)
      for row in triangle:
            print(" "*(n-len(row))+" ".join(map(str,row)))
pascals_triangle()

# Problem 1
def pattern_integer():
      n=int(input('Enter a number: '))
      for i in range(n):
            print(''.join(str(i) for i in range(1,n+1)))
pattern_integer()

# Problem 2
def pattern_increase():
      n=int(input('Enter a number: '))
      for i in range(n):
            for j in range(n):
                  print(i+j+1,end='')
            print()
pattern_increase()

# Problem 3
def pattern_increase():
      n=int(input('Enter a number: '))
      for i in range(1,n+1):
            for j in range(i,i+i):
                  print(j,end='')
            print()
pattern_increase()

# Problem 5
def decreasing_pattern():
      n=int(input('Enter a number: '))
      for i in range(n,0,-1):
            for j in range(n,i-1,-1):
                  print(j,end='')
            print()
decreasing_pattern()

# Problem 6
def integer_pattern():
      n=int(input('Enter a number: '))
      for i in range(1,n+1):
            for j in range(1,i+1):
                  print(j,end='')
            print()
integer_pattern()

# Problem 7
def print_star():
      n=int(input('Enter a number: '))
      for i in range(n):
            for j in range(n):
                  print('*',end='')
            print()
print_star()

# Problem 8
def print_star():
      n=int(input('Enter a number: '))
      for i in range(n,0,-1):
            for j in range(i,0,-1):
                  print('*',end='')
            print()
print_star()
