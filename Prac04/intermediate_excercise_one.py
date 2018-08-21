numbers = []
print("Please enter 5 numbers:")
for i in range(1,6):
    user_input = int(input("Number {}: ".format(i)))
    numbers.append(user_input)
print("The first number is {}.".format(numbers[0]))
print("The last number is {}.".format(numbers[4]))
print("The smallest number is {}.".format(min(numbers)))
print("The largest number is {}.".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))
