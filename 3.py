def print_alphabet_triangle(rows):
  """Prints a right-angled triangle pattern of alphabets.

  Args:
    rows: The number of rows in the triangle.
  """
  for i in range(1, rows + 1):
    output = ""
    for j in range(i):
      output += chr(ord('A') + j)
    print(output)

# Let's print an alphabet triangle with 5 rows, just like your example
print_alphabet_triangle(5)