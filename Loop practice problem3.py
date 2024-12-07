n=int(input('Enter a number to start the loop: '))
n1=1
for i in range(n):
      print(n1,end="," if i!=n-1 else" ")
      n1=1-n1