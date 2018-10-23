def main():
    user_input = int(input("Please enter the number of rows: "))
    number_of_rows = user_input
    number_of_blocks = calculate_number_of_blocks(number_of_rows)
    print(number_of_blocks)


def calculate_number_of_blocks(number_of_rows):
    if number_of_rows <= 0:
        return 0
    number_of_blocks = number_of_rows + calculate_number_of_blocks(number_of_rows - 1)
    return number_of_blocks


main()