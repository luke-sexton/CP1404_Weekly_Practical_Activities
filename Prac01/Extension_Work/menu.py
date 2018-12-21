MENU = "(H)ello \n(G)oodbye \n(Q)uit"

user_name = input("Enter name: ")
print(MENU)
user_choice = input(">>> ").upper()

while user_choice != 'Q':
    if user_choice == "H":
        print("Hello", user_name)
    elif user_choice == "G":
        print("Goodbye", user_name)
    else:
        print("Invalid choice")
    print(MENU)
    user_choice = input(">>> ").upper()
print("Finished.")
