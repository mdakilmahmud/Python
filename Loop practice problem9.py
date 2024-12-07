# Solution 1
x=input('Enter a string: ')
vowels='aeiouAEIOU'
vowel_count=0
for char in x:
      if char in vowels:
            vowel_count=vowel_count+1
print(f'Number of vowels: {vowel_count}')

# Solution 2
x=input('Enter a string: ')
vowels='aeiouAEIOU'
vowel_count=0
for char in x:
      if char in vowels:
            vowel_count += 1
            
print(f'Number of vowels: {vowel_count}')