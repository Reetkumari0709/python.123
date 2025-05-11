def print_number_triangle(rows):
  """Prints a right-angled triangle pattern of numbers.

  Args:
    rows: The number of rows in the triangle.
  """
  for i in range(1, rows + 1):
    output = ""
    for j in range(1, i + 1):
      output += str(j)
    print(output)

# Let's print a number triangle with 5 rows, just like your example
print_number_triangle(5)