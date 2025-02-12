# 1
def sort_dict_by_value(dictionary):
    items = list(dictionary.items())
    def get_value(item):
        return item[1]
    sorted_items = sorted(items, key=get_value)
    sorted_items.reverse()
    return sorted_items
sample_input = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
print(sort_dict_by_value(sample_input))

#
sample_input = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
items = list(sample_input.items())
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]
print(items)

# 2
def ListoDictionary(list):
    new_dictionary={}
    for item in list:
        key=item["item"]
        value=item["amount"]
        if key in new_dictionary:
            new_dictionary[key]+=value
        else:
            new_dictionary[key]=value
    return new_dictionary
data=[{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}]
print(ListoDictionary(data))

#
data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]
combined_values = {}
for entry in data:
    item = entry['item']
    amount = entry['amount']  
    if item in combined_values:
        combined_values[item] += amount
    else:
        combined_values[item] = amount
print(combined_values)

# 3
def stringCount(string):
    new_dict={}
    for i in string:
        if i in new_dict:
            new_dict[i]+=1
        else:
            new_dict[i]=1
    return new_dict
string_input=str(input("Enter a string: "))
print(stringCount(string_input))

#
string_input=str(input("Enter a string: "))
new_dict={}
for i in string_input:
    if i in new_dict:
        new_dict[i]+=1
    else:
        new_dict[i]=1
print(new_dict)

# 4
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
new_dict = {}
for key in keys:
    if key in sample_dict:  
        new_dict[key] = sample_dict[key]
print(new_dict)

def keytoextract(key1,key2):
    keys=[key1,key2]
    return keys
def extractkey(dictionary,keys):
    new_dict={}
    for key in keys:
        if key in dictionary:
            new_dict[key]=dictionary[key]
    return new_dict
sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}
key=keytoextract("name", "salary")
print(extractkey(sample_dict,key))

# 5
def convert_to_dict_list(color_names, color_codes):
    result = []
    for name, code in zip(color_names, color_codes):
        result.append({'color_name': name, 'color_code': code})
    return result
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
output = convert_to_dict_list(color_names, color_codes)
print(output)

#
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result = []
for name, code in zip(color_names, color_codes):
      result.append({'color_name': name, 'color_code': code})
print(result)

# 6
def frequencyCount(sentence):
    words=sentence.split()
    new_dict={}
    for word in words:
        if word in new_dict:
           new_dict[word]+=1
        else:
            new_dict[word]=1
    return new_dict
sentence=input("Enter a string: ")
print(frequencyCount(sentence))

# 
sentence=input("Enter a string: ")
words=sentence.split()
new_dict={}
for word in words:
      if word in new_dict:
            new_dict[word]+=1
      else:
            new_dict[word]=1
print(new_dict)

# 7
def oddinteger(list):
      odd_number=[]
      for i in list:
            if i%2!=0:
                 odd_number.append(i)
      return odd_number
def getSquare(odd_number):
      new_dict={}
      for i in odd_number:
            new_dict[i]=i*i
      return new_dict
data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(getSquare(oddinteger(data)))

#
data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers=[]
new_dict={}
for i in data:
      if i%2!=0:
            odd_numbers.append(i)
for i in odd_numbers:
    new_dict[i]=i*i
print(new_dict)
# 8
def transformData(dictionary,key1,key2):
      new_dict={}
      for key,value in dictionary.items():
            new_dict[key] = {key1: value[key1], key2: value[key2]}
      return new_dict
original_data = {
'Emma': {'name': 'Emma', 'major': 'Computer Science', 'cgpa': 3.8, 'completed_credits': 90},
'Daniel': {'name': 'Daniel', 'major': 'Electrical Engineering', 'cgpa': 3.5, 'completed_credits': 75},
'Sophia': {'name': 'Sophia', 'major': 'Mechanical Engineering', 'cgpa': 3.2, 'completed_credits': 60}
}
print("Transformed student data:")
print(transformData(original_data, 'cgpa', 'completed_credits'))
#
original_data = {
'Emma': {'name': 'Emma', 'major': 'Computer Science', 'cgpa': 3.8, 'completed_credits': 90},
'Daniel': {'name': 'Daniel', 'major': 'Electrical Engineering', 'cgpa': 3.5, 'completed_credits': 75},
'Sophia': {'name': 'Sophia', 'major': 'Mechanical Engineering', 'cgpa': 3.2, 'completed_credits': 60}
}
new_dict={}
key1="cgpa"
key2="completed_credits"
for key,value in original_data.items():
      new_dict[key] = {key1: value[key1], key2: value[key2]}
print(new_dict)
# 9
company_hr_register = {
    101: {'name': 'Alice', 'age': 35, 'performance': 90, 'salary': 50000},
    102: {'name': 'Bob', 'age': 58, 'performance': 98, 'salary': 70000},
    103: {'name': 'Charlie', 'age': 45, 'performance': 85, 'salary': 60000},
    104: {'name': 'David', 'age': 60, 'performance': 75, 'salary': 55000},
    105: {'name': 'Eve', 'age': 28, 'performance': 92, 'salary': 48000},
    106: {'name': 'Frank', 'age': 50,'performance': 55, 'salary': 52000},
    107: {'name': 'Grace', 'age': 62,'performance': 97, 'salary': 75000},
}
total_bonus_amount = 0
updated_company_hr_register = {}
for key, value in company_hr_register.items():
    age = value['age']
    performance = value['performance']
    if performance < 60:
      continue
    bonus=0
    if age > 55:
        bonus += 10000
    if performance > 95:
        bonus += 5000
    updated_company_hr_register[key] = {'name': value['name']}
    total_bonus_amount += bonus
total_employees = len(updated_company_hr_register)
print(f"total_employees = {total_employees}")
print(f"total_bonus_amount = {total_bonus_amount}")
print("updated_company_hr_register =")
print(updated_company_hr_register) 