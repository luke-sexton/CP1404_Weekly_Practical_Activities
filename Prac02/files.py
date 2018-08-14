# 1
output_file = "name.txt"
out_file = open(output_file, 'w')

user_name = input("Please enter your name: ")
print("Your name is", user_name, file=out_file)
out_file.close()

# 2
name_file = open("name.txt", 'r')
first_line = name_file.readline()
print(first_line)
name_file.close()

# 3
numbers_file = open("numbers.txt", 'r')

num_one = int(numbers_file.readline())
num_two = int(numbers_file.readline())
total = num_one + num_two
print(total)

numbers_file.close()

with open("numbers.txt") as numbers_file:
    numbers = numbers_file.readlines()

total = 0
for number in numbers:
    total += int(number)
print(total)
