user_character = input("Enter a character (it is case sensitive): ")
print("The ASCII code for", user_character, "is", ord(user_character))

user_number = int(input("Enter a number between 33 and 127: "))
valid_input = False
while not valid_input:
    if 33 <= user_number <= 127:
        print("The character for", user_number, "is", chr(user_number))
        valid_input = True
    else:
        user_number = int(input("Enter a number between 33 and 127: "))
