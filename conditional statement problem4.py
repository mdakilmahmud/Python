employees_salary=int(input('Enter thr employees salary: '))
if employees_salary<20000:
      print(f'After the increment the employees salary will be: {employees_salary+(employees_salary*15/100)}')
elif employees_salary<=50000:
      print(f'After the increment the employees salary will be: {employees_salary+(employees_salary*10/100)}')
elif employees_salary<=70000:
      print(f'After the increment the employees salary will be: {employees_salary+(employees_salary*8/100)}')
elif employees_salary>70000:
      print(f'After the increment the employees salary will be: {employees_salary+(employees_salary*5/100)}')
elif employees_salary<10000 or employees_salary>200000:
      print('You will not get an increment')     
