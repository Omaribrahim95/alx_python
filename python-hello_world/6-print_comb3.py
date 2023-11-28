for first_digit in range(10):
  for second_digit in range(first_digit + 1, 10):
    if first_digit * 10 + second_digit < second_digit * 10 + first_digit:
      print("{0:02d}, ".format(first_digit * 10 + second_digit), end="")
print()