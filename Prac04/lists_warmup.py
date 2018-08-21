numbers = [3, 1, 4, 1, 5, 9, 2]

#1
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
if 5 in numbers:
    print("Yes")
else:
    print("No")
if 7 in numbers:
    print("Yes")
else:
    print("No")
if "3" in numbers:
    print("Yes")
else:
    print("No")
#2
numbers[0] = 10
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[1:])
if 9 in numbers:
    print("9 is in numbers")
else:
    print("( is not in numbers")

"""numbers + [6, 5, 3] Check in console"""
