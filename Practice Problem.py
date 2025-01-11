# Problem 1
def max_of_three(a, b, c):
      if a>=b and a>=c:
            return a
      elif b>=a and b>=c:
            return b
      else:
            return c
result=max_of_three(5,10,3)
print(f'Expected Output: {result}')

# Another Question related to this problem 
# Write a Python program that firstly it will ask the user how many numbers 
# he wants to give as input and then the program will take the numbers
# as many as the user wised before as n1,n2,n3...... and then among 
# all the numbers it will find the max number
def find_max_number():
      count=int(input('How many numbers you want to give as input: '))
      if count<1:
            print('You need to input at least one number.')
            return
      number=[]
      print(f'Enter {count} numbers: ')
      for i in range(count):
            num=float(input(f'Number {i+1}: '))
            number.append(num)
      max_number=max(number)
      print(f'The maximum number among the inputs is: {max_number}') 
find_max_number()     

# Problem 2
def sum_of_number():
      number=[8,2,3,0,7]
      sum_numbers=0
      for i in number:
            sum_numbers+=i
      print(sum_numbers)
sum_of_number()

# Another Question Related to this problem
# Write a Python program that will firstly it will ask the user how many 
# numbers he wants to give as input and then the program will take the 
# numbers as many as the user wised before as n2, n3...... and then 
# among all the numbers it will find the max number to the less max 
# number, and it will show respectively and then give the sum of them.
def sum_of_number():
      count=int(input('How many numbers you want to input? : '))
      if count<1:
            print('You need to input at least one number.')
      numbers=[]
      print(f'Enter {count} numbers: ')
      for i in range(count):
            num=int(input(f'Number {i+1}: '))
            numbers.append(num)
      sum_number = sum(numbers)
      print(f'The sum of the numbers is: {sum_number}')
sum_of_number()

# Problem 3
def multiply_the_numbers():
      list=[8, 2, 3, -1, 7]
      multiply_number=1
      for i in list:
            multiply_number*=i
      print(multiply_number)
multiply_the_numbers()

# Another Question Related to this problem
# Write a Python program that will firstly it will ask the user how 
# many numbers he wants to give as input and then the program will take 
# the numbers as many as the user wised before as n2, n3...... and then 
# among all the numbers it will find the max number to the less max  
# number, and it will show respectively and then give the sum and 
# multiplication of them.
def all_works():
      def get_numbers():
            count=int(input('How many numbers you want to input? : '))
            if count<1:
                  print('You need to input at least one number.')
                  return[]
            number=[]
            print(f'Enter {count} numbers:')
            for i in range(count):
                  num=int(input(f'Number {i+1}: '))
                  number.append(num)
            return number
      def calculate_number(number):
            sorted_numbers=sorted(number,reverse=True)
            print('Numbers from max to less max:',end='')
            print(sorted_numbers)
            total_sum=sum(sorted_numbers)
            total_product=1
            for num in sorted_numbers:
                  total_product*=num
            print(f"Sum of numbers: {total_sum}")
            print(f"Multiplication of numbers: {total_product}")
      number=get_numbers()
      if number:
            calculate_number(number)
all_works()

# Problem 4
def string_reverse():
    inpu=input('Enter your string: ')
    reverse_string=inpu[::-1]
    print(f'Reversed String: {reverse_string}')
string_reverse()

# Another Question Related to this problem
# Write a Python program that takes input from the user as a string 
# and find the index for each string.
def index_search():
      string=(input('Enter your string: '))
      print('Index number of the strings are:')
      for char in range(len(string)):
            print(f"Character: {string[char]} at index: {char}")
index_search()

# Another Question Related to this problem
# Write a Python program that counts the frequency of each character 
# in a given string.
# Sample Input: "aabbccdd"
# Character: 'a', Count: 2
# Character: 'b', Count: 2
# Character: 'c', Count: 2
# Character: 'd', Count: 2
def frequency_count():
      string=input('Enter your string: ')
      frequency={}
      for char in string:
            if char in frequency:
                  frequency[char]+=1
            else:
                  frequency[char]=1
      for char,count in frequency.items():
            print(f"Character: {[char]}, count: {count}")
frequency_count()

# Problem 5
def get_factorial():
      num=int(input('Enter a number: '))
      fac=1
      for i in range(1,num+1):
            fac*=i
      print(fac)
get_factorial()


# Problem 6
# Problem 7
def check_upper_lower():
      string=str(input('Enter your stirng: '))
      upper_count=0
      lower_count=0
      for char in string:
            if char.isupper():
                  upper_count+=1
            elif char.islower():
                  lower_count+=1
      print(f'No. of Upper case characters: {upper_count}, No. of lower case characters: {lower_count}')
check_upper_lower()

# Problem 8
def unique_list():
      x=list(map(int,input('Enter the elements separated by space = ').split()))
      uni_list=[]
      for i in x:
            if i in uni_list:
                  continue
            else:
                  uni_list.append(i)
      return uni_list
print(unique_list())

# Another Solution
def isduplicate():
    items = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True  
            return False
print(f"This list contains duplicates: {isduplicate()}")

# Problem 9
def is_prime():
    n=int(input('Enter a number: '))
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime())

# Problem 10
def find_even_number():
    x = list(map(int, input('Enter numbers separated by space: ').split()))
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i)
    return y
print(find_even_number())

# Problem 11
def check_perfect_number():
      num=int(input('Enter a number: '))
      sum=0
      for i in range(1,num):
            if num%i==0:
                  sum+=i
            if sum==num:
                  print(f'The number {num} is a Perfect Number')
      else:
           print(f'The number {num} is not a Perfect Number') 
check_perfect_number()

# Problem 12
def find_palindrome():
      string=str(input('Enter your string: '))
      for i in range(string):
            if string%i==0:
                  sum+=i
      if sum==string:
            print(f'The string {string} is a palindrome')
      else:
            print(f'The string {string} is a palindrome')
find_palindrome()