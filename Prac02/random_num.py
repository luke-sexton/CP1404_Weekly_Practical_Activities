import random

print(random.randint(5, 20))
# Smallest number = 5 - Largest number = 20
print(random.randrange(3, 10, 2))
# Smallest number = 3 - Largest number = 9 - Cannot produce 4 as it is counting in steps of 2.
print(random.uniform(2.5, 5.5))
# Smallest number = 2.50001 - Largest number = 5.49999999
