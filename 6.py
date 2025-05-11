def reverse_number(num):
  """Reverses a given integer using arithmetic operations.

  Args:
    num: The integer to be reversed.

  Returns:
    The reversed integer.
  """
  reversed_num = 0
  while num > 0:
    remainder = num % 10  # Get the last digit
    reversed_num = (reversed_num * 10) + remainder  # Build the reversed number
    num //= 10  # Remove the last digit from the original number
  return reversed_num

# Get input from the user
input_number = int(input("Enter a number: "))

# Reverse the number
reversed_output = reverse_number(input_number)

# Print the output
print("Input :", input_number)
print("Output:", reversed_output)