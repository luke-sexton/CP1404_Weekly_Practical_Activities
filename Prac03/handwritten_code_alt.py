"""Practical 03: handwritten_code alternative - Refactor Method"""

MINIMUM_LENGTH = 4


def main():
    """Get a password of valid size and print asterisks."""
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


main()
