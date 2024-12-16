# Problem 1
length = float(input('Enter the length = '))
width = float(input('Enter the width = '))
area=length*width
perimeter=2*(length+width)
print(f'Area = {area}, Perimeter = {perimeter}')

# Problem 2
n1=float(input('Enter the first number = '))
n2=float(input('Enter the second number = '))
n3=float(input('Enter the third number = '))
print(f'Average = {(n1+n2+n3)/3}')

# Problem 3
n1=float(input('Enter the first number = '))
n2=float(input('Enter the second number = '))
print(f'Quotient = {n1//n2}, Remainder = {n1%n2}')

# Problem 4
radius=int(input('Enter a number = '))
value_of_pi=3.1416
print(f'Circumference = {radius*value_of_pi*2}, Area = {value_of_pi*radius**2}')

# Problem 5
duration=int(input('Enter the time in Seconds = '))
minutes=duration//60
hour=minutes//60
print(f'Minutes = {minutes}, Hours = {hour}')

# Problem 6
price=float(input('Enter the book price = '))
print(f'Price after 20% discount: {price-(price*20/100)}')

# Problem 7
num=int(input('Enter a number = '))
print(f'The last digit is: {num%10}')