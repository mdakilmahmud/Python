datalist = [1452, 11.23, 1+2j, True,'Pikachu', (0, -1), [5, 12],{"Type":'Electric', "Ability":'Static'}]
for item in datalist:
  print(f'Type of item {item} is <class {type(item)}>')