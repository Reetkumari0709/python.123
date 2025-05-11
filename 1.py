def print_reverse_triangle(rows):
  """Prints an inverted right-angled triangle pattern of stars.

  Args:
    rows: The number of rows in the triangle.
  """
  for i in range(rows, 0, -1):
    print("*" * i)

# Let's print a reverse triangle with 5 rows, just like your example
print_reverse_triangle(5)