
numbers = [12, 37, 74, 45, 67, 89, 70, 23, 17, 56]

result = []

for num in numbers:
    for char in str(num):
        if char == '7': 
            result = result + [num] 
            break

print("The numbers containing 7: ", result)
