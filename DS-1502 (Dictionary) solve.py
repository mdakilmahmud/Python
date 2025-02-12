# 1a
def lterateOver(data):
      for key, value in data.items():
            print(f"{key}: {value}")
data={ 
    "Iron Man": "Tony Stark", 
    "Captain America": "Steve Rogers", 
    "Thor": "God of Thunder", 
    "Hulk": "Bruce Banner" 
}
lterateOver(data)

# 1b
def lterateOver(dictionary):
      for key,value in dictionary.items():
            print(f"{key}: {value}")
data={ 
    "Pikachu": "Electric", 
    "Charmander": "Fire", 
    "Squirtle": "Water", 
    "Bulbasaur": "Grass/Poison" 
}
lterateOver(data)

# 2
def MaximumandMinimum(dictionary):
      max_value=max(dictionary.values())
      min_value=min(dictionary.values())
      print(f"Maximum Value: {max_value}")
      print(f"Minimum Value: {min_value}")
data={'x': 500, 'y': 5874, 'z': 560}
MaximumandMinimum(data)

# 3
def findInput(dictionary,key):
      return key in dictionary
marvel = {"Iron Man": "Tony Stark",
    "Captain America": "Steve Rogers",
    "Thor": "God of Thunder",
    "Hulk": "Bruce Banner"}
key_input=input("Enter the first key to check: ")
print(f"Does '{key_input}' exist? {findInput(marvel, key_input)}")

# 4
def mergeDictionary(dict1,dict2):
      dict1.update(dict2)
      return dict1
dict1 = {"name": "Alice", "age": 25} 
dict2 = {"city": "Wonderland", "age": 30}
mergeDictionary(dict1,dict2)

# 5
dict_list = [ 
    {"a": 10, "b": 20}, 
    {"a": 30, "b": 40}, 
    {"a": 50, "b": 60} 
]
result={}
for i in dict_list:
      for key,value in i.items():
            if key not in result:
                result[key] = 0
            result[key] += value
print(result)

def sum_dict_values(dict_list):
    result = {}  
    for d in dict_list: 
        for key, value in d.items():  
            if key not in result:
                result[key] = 0  
            result[key] += value
            return result
dict_list = [ 
    {"a": 10, "b": 20}, 
    {"a": 30, "b": 40}, 
    {"a": 50, "b": 60} 
]
print(sum_dict_values(dict_list))

# 6
dictionary={"Harry":"Gryffindor","Dobby":None,
            "Nearly Headless Nick": "Gryffindor",
            "Snape":"Slytherin","Cedric":"Hufflepuff",
            "Peeves the Poltergeist":None}
new_dictionary={}
for key,value in dictionary.items():
      if value is not None:
            new_dictionary[key]=value
print(new_dictionary)

def remove_none_values(dictionary):
    new_dictionary = {}  
    for key, value in dictionary.items():
        if value is not None:  
            new_dictionary[key] = value 
    return new_dictionary 
dictionary = {
    "Harry": "Gryffindor",
    "Dobby": None,
    "Nearly Headless Nick": "Gryffindor",
    "Snape": "Slytherin",
    "Cedric": "Hufflepuff",
    "Peeves the Poltergeist": None
}
print(remove_none_values(dictionary))

# 7
def getHighestvalue(dictionary):
      max_value=max(dictionary.values())
      max_key=""
      for key,value in dictionary.items():
            if value == max_value:
                  max_key=key
      print(f"The Highest Selling Book genre is {max_key} and the number of books sold are {max_value}")
book_shop = {
      'sci fi': 12, 'mystery': 15, 'horror': 8, 
      'mythology': 10, 'young_adult': 4, 'adventure':14
      }
getHighestvalue(book_shop)

def getHighestvalue(dictionary):
    max_value = 0 
    max_key = "" 
    for key, value in dictionary.items():
        for v in dictionary.values():  
            max_value = max(dictionary.values())  
        if dictionary[key] == max_value:  
            max_key = key
    print(f"The Highest Selling Book genre is {max_key} and the number of books sold are {max_value}")
getHighestvalue({'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure': 14})

# 8
def find_eye_color(info):
    return info['personal_data']['physical_features']['color']['eye']
def find_fav_color_starting_with_vowel(info):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for color in info['other']['favorite_colors']:
        if color[0].lower() in vowels:
            return color
        else:
            return False
def find_areas_of_interest(info):
    interests = info['other']['interested_in']
    return len(interests), interests
def check_interest_in_gadgets(info):
    interests = info['other']['interested_in']
    for interest in interests:
        if interest == 'gadgets':
            return True
    return False
def check_height_greater_than_5_feet(info):
    height = float(info['personal_data']['physical_features']['height'])
    if height > 5:
        return True
    return False
info = { 
'personal_data': {'name': 'Lauren', 'age': 20, 'major': 'Information Science', 
'physical_features': {'color': {'eye': 'blue', 'hair': 'brown'}, 'height': "5.8"}}, 
'other': {'favorite_colors': ['purple', 'green', 'blue', 'indigo'], 
'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']} 
}
print("Eye Color:", find_eye_color(info))
print("Favorite color starting with a vowel:", find_fav_color_starting_with_vowel(info))
num_interests, interests = find_areas_of_interest(info)
print("Number of Areas of Interest:", num_interests)
print("Interests:", interests)
print("Interested in Gadgets:", check_interest_in_gadgets(info))
print("Height greater than 5 feet:", check_height_greater_than_5_feet(info))

# 
info = { 
'personal_data': {'name': 'Lauren', 'age': 20, 'major': 'Information Science', 
'physical_features': {'color': {'eye': 'blue', 'hair': 'brown'}, 'height': "5.8"}}, 
'other': {'favorite_colors': ['purple', 'green', 'blue', 'indigo'], 
'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']} 
}
eye_colour = info['personal_data']['physical_features']['color']['eye']
vowel=('a','e','i','o','u')
fav_color_with_vowel = False
for color in info['other']['favorite_colors']:
    if color[0].lower() in vowel:
        fav_color_with_vowel = color
    break
interest=info['other']['interested_in']
interest_in_gadgets = False
for interests in interest:
    if interest == 'gadgets':
        interest_in_gadgets = True
    break
height=float(info['personal_data']['physical_features']['height'])
height_greater_than_5_feet = height > 5
print(f"Eye Color: {eye_colour}")
print(f"Favorite color starting with a vowel: {fav_color_with_vowel}")
print(f"Number of Areas of Interest: {len(interest)}")
print(f"Interests: {interest}")
print(f"Interested in Gadgets: {interest_in_gadgets}")
print(f"Height greater than 5 feet: {height_greater_than_5_feet}")

# 9
def stringcount(string):
      count_string={}
      for i in input_string:
            if i!=" ":
                  if i in count_string:
                        count_string[i]+=1
                  else:
                        count_string[i]=1
      return count_string
input_string=input("Enter a string: ")
print(stringcount(input_string))

# 10
def dictionarytolist(dictionary):
      new_list=[]
      for key,value in dictionary.items():
            new_list.append([key]+value)
      return new_list
friends_dict = { 
    "Rachel Green": [25, "Fashion Designer"], 
    "Ross Geller": [27, "Paleontologist"], 
    "Monica Geller": [26, "Chef"], 
    "Chandler Bing": [28, "Statistical Analyst"], 
    "Joey Tribbiani": [29, "Actor"], 
    "Phoebe Buffay": [26, "Musician"] 
}
print(dictionarytolist(friends_dict))

# 11
def sorteDictionary(dictionary):
    sort_key = dict(sorted(dictionary.items()))
    sort_value = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    print("Sorted by Keys:", sort_key)
    print("Sorted by Values:", sort_value)
sample_dict = {'apple': 5, 'banana': 2, 'orange': 3, 'grape': 4}
sorteDictionary(sample_dict)


# 12a
def extractValues(no_list,key):
    new_list=[]
    for item in no_list:
        if key in item:
            new_list.append(item[key])
    return new_list
no_list=[ 
{"character": "Wednesday Addams", "trait": "Dark humor"}, 
{"character": "Enid Sinclair", "trait": "Cheerful"}, 
{"character": "Thing", "trait": "Helpful"}, 
{"character": "Xavier Thorpe", "trait": "Artistic"} 
]
print(extractValues(no_list,"character"))

# 12b
def extractValues(no_list,key):
    new_list=[]
    for item in no_list:
        if key in item:
            new_list.append(item[key])
    return new_list
no_list=[ 
{"character": "Eleven", "power": "Telekinesis"}, 
{"character": "Mike Wheeler", "power": "Loyalty"}, 
{"character": "Will Byers", "power": "Survival"}, 
{"character": "Max Mayfield", "power": "Bravery"} ]
print(extractValues(no_list,"power"))

# 13a
def findFloor(num):
    return int(num)
def floorDictionay(list,func):
    new_dict={}
    for i in list:
        key=func(i)
        new_dict.setdefault(key,[]).append(i)
    return new_dict
given_list = [7, 23, 3.2, 3.3, 8.4]
print(floorDictionay(given_list, findFloor))

# 13b
def LenNumber(num):
    return len(num)
def FloorDictionary(list,func):
    new_dict={}
    for i in list:
        key=func(i)
        new_dict.setdefault(key,[]).append(i)
    return new_dict
given_list=['Red', 'Green', 'Black', 'White', 'Pink']
print(FloorDictionary(given_list,LenNumber))

# 14
nested_dict = {'a': {'key': 3}, 'b': {'key': 1}, 'c': {'key': 2}}
sorted_items = sorted(nested_dict.items(), key=lambda item: item[1]['key'])
sorted_dict = {}
for key, value in sorted_items:
    sorted_dict[key] = value
print(sorted_dict)

# 15
original_list = [('Rabbit', 7), ('Elephant', 15), ('Squirrel', 3), ('Cat', 9), ('Dog', 12)]
converted_dict = dict(original_list)
sorted_dict = dict(sorted(converted_dict.items(), key=lambda item: item[1], reverse=True))
print("Converted Dictionary:", converted_dict)
print("Sorted Dictionary (descending):", sorted_dict)