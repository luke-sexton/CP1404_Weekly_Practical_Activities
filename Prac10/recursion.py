"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


print(do_it(5))


# 1. write down what you think the output of this will be,
# Output (n = 5): 3
# 2. use the debugger to step through and see what's actually happening


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n >= 0:
        print(n ** 2)
        do_something(n - 1)


print(do_something(4))
# 3. write down what you think the output of do_something(4) will be,
# Output:
# 16
# 9
# 4
# 1
# 0
# 4. use the debugger to step through and see what's actually happening


# fix do_something() so that it works according to the docstring
