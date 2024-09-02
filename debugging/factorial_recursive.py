#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the integer n. Returns 1 if n is 0 (because 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Read the integer from the command line arguments
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)
