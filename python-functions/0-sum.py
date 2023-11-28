import time

def add(a, b):
    """Adds two integers and returns the result."""
    result = a + b
    return result

# Generate two random integers using time.time() as a seed
a = int(time.time() * 1000) % 100 + 1
b = int(time.time() * 1000) % 100 + 1

# Add the two integers and print the result
print(add(a, b))