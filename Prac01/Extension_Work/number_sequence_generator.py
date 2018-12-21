MENU = "1. Show the even numbers \n" \
       "2. Show the odd numbers \n" \
       "3. Show the squares \n" \
       "4. Exit the program "
QUIT_APPLICATION = 4

starting_number = int(input("Enter Starting Number: "))
finishing_number = int(input("Enter Finishing Number : "))

print(MENU)
user_choice = int(input(">>> "))
while user_choice != QUIT_APPLICATION:
    if user_choice == 1:
        even_numbers = [number for number in range(starting_number, finishing_number + 1) if number % 2 == 0]
        for number in even_numbers:
            print(number, end=" ")
        print()
    elif user_choice == 2:
        odd_numbers = [number for number in range(starting_number, finishing_number + 1) if number % 2 == 1]
        for number in odd_numbers:
            print(number, end=" ")
        print()
    elif user_choice == 3:
        squared_numbers = [number ** 2 for number in range(starting_number, finishing_number + 1)]
        for number in squared_numbers:
            print(number, end=" ")
        print()
    else:
        print("Invalid choice")

    print(MENU)
    user_choice = int(input(">>> "))
