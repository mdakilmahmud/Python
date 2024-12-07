n=int(input('Enter a number to start the loop: '))
for i in range(1,n,2):
      if i!=n-1:
            print(i,end=", ")
      else:
            print(i)