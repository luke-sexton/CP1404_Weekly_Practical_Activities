LOWER = 33
UPPER = 127

user_character = input("Enter a character (it is case sensitive): ")
print("The ASCII code for", user_character, "is", ord(user_character))

user_number = int(input("Enter a number between " + str(LOWER) + " and " + str(UPPER) + ": "))

valid_input = False
while not valid_input:
    if LOWER <= user_number <= UPPER:
        print("The character for", user_number, "is", chr(user_number))
        valid_input = True
    else:
        user_number = int(input("Enter a number between " + str(LOWER) + " and " + str(UPPER) + ": "))

