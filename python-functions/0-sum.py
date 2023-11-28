#!/usr/bin/env python3
def add(a, b):
  """
  Adds two integers and returns the result.

  Args:
    a: The first integer to add.
    b: The second integer to add.

  Returns:
    The sum of a and b.
  """
  return a + b

add = __import__('0-sum').add
# Test the function
print(add(1, 2))  # Output: 3
print(add(98, 0))  # Output: 98
print(add(100, -2))  # Output: 98