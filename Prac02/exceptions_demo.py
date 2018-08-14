"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If value = any character that is not a number e.g - letter

2. When will a ZeroDivisionError occur?
If denominator = 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

                        ***HELP***

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
