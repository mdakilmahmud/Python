list_input=float(input('Enter the elements of the list: '.split(',')))
list_numbers = [int(num) for num in list_input]
n=float(input('Eneter the number you want to find: '))
if n==list_numbers:
      print('Present')
else:
      print('Not present')