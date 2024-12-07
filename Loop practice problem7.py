# Solution 1 
input_string = input("Enter a string: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string 
print(f"Reversed string: {reversed_string}")

# Solution 2
input_string = input("Enter a string: ")
for i in range(len(input_string),0,-1):
    print(input_string[i-1], end="")