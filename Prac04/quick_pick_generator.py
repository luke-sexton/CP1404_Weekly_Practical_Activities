import random

NUMBER_AMOUNT = 6
MIN = 1
MAX = 45

user_input = int(input('How many "quick picks" would you like to generate? '))
while user_input < 0:
    print("Invalid number")
    user_input = int(input('How many "quick picks" would you like to generate? '))

for line in range(user_input):
    generate_numbers = []
    for num in range(NUMBER_AMOUNT):
        number = random.randint(MIN, MAX)
        while number in generate_numbers:
            number = random.randint(MIN, MAX)
        generate_numbers.append(number)
    print(" ".join("{:2}".format(number) for number in generate_numbers))