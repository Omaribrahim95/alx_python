import random

def add(a, b):
    """Adds two integers and returns the result."""
    result = a + b
    return result

# Generate two random integers
a = random.randint(1, 100)
b = random.randint(1, 100)

# Add the two integers and print the result
print(add(a, b))