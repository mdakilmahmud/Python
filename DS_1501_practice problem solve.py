# 1(a)
a,b=6,9
if a>b:
      diff=a-b
      print(f'Differece = {diff}')
else:
      sum=a+b
      print(f'Sum = {sum}')

# 1(b)
hi = 0
hlw = 10
num = [10, 20, 30, 40]
hlw =len(num)
for i in range(hlw,6):
      print(i)
      if hi < len(num) - 1:
            num[hi] = num[hi + 1] - 5
            hi += 1
            print(num)
      hlw -= 2
print(num[-4:-1])

# 2(a)
total_power = float(input("Enter the total power of the Hashiras: "))
num_hashiras = int(input("Enter the number of Hashiras: "))
demon_rank = input("Enter the Upper Moon demon’s rank (if any, 1-6; else leave blank): ").strip()
if demon_rank in ['1', '2', '3']:
        total_power *= 0.7  
elif demon_rank in ['4', '5', '6']:
        total_power *= 0.8 
print(f"Total Power of Hashiras after reduction: {total_power}")
if demon_rank in ['1', '2', '3']:
        if num_hashiras >= 3 and total_power >= 3000:
            print("Demon Defeated: Yes")
        else:
            print("Demon Defeated: No")
elif demon_rank in ['4', '5', '6']:
        if num_hashiras >= 2 and total_power >= 2000:
            print("Demon Defeated: Yes")
        else:
            print("Demon Defeated: No")
else:
        if num_hashiras >= 1 and total_power >= 1000:
            print("Demon Defeated: Yes")
        else:
            print("Demon Defeated: No")

# 2(b)
special_grade_list = ["sukuna's finger", "cursed womb", "black rope"]
semi_grade_list = ["cursed Painting", "playful cloud", "black rope"]
cursed_object = input("Enter the name of the cursed object: ")
if cursed_object in special_grade_list and cursed_object in semi_grade_list:
    print("Exists in both lists.")
elif cursed_object in special_grade_list:
    print("Exists in special-grade list.")
elif cursed_object in semi_grade_list:
    print("Exists in semi-grade list.")
else:
    print("Does not exist in either list.")

# 3
rows = 3
cols = 5
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print('*', end='')
        else:
            print('', end='')
    print()
# output: 
'''*
   **
   **'''

# 4
n = 3
for i in range(1, n + 1):
      for j in range(1, (n + i - 1) + 1):
            if j <= n - i:
                  print(" ", end = "")
            else:
                  print("*", end = "")
      print()
for i in range(n - 1, 0, -1):
      for j in range(1, (n + i - 1) + 1):
            if j <= n - i:
                  print(" ", end = "")
            else:
                  print("*", end = "")
print()
# Output: 
'''  *
    ***
   *****
    ***  *'''

# 5
total_cost = int(input('Enter the total cost: '))
total_weight = int(input('Enter the weight of items: '))
discount_code = str(input('Enter the discount code (if any): '))
if total_cost < 50 and total_weight <= 5:
    delivery_charge = 5
    total_amount = total_cost + delivery_charge
elif total_cost < 50 and total_weight > 5:
    delivery_charge = 15
    total_amount = total_cost + delivery_charge
elif 50 <= total_cost < 100 and total_weight <= 5:
    delivery_charge = 20
    total_amount = total_cost + delivery_charge
elif 50 <= total_cost < 100 and total_weight > 5:
    delivery_charge = 25
    total_amount = total_cost + delivery_charge
else:
    delivery_charge = 30
    total_amount = total_cost + delivery_charge
if discount_code == "SAVE10":
    total_amount = total_amount - (total_amount * 10 / 100)
print(f"Total amount: {total_amount}")

# 6
numbers = [10, 20, 30, 40, 50]
i = 0
while i < len(numbers) - 1:
      temp = numbers[i]
      numbers[i] = numbers[i + 1]
      numbers[i + 1] = temp
      i += 2
print("List after swapping:", numbers)