def gcd_loop(a, b):
  """
  Calculates the Greatest Common Divisor (GCD) of two numbers using a loop.

  Args:
    a: The first integer.
    b: The second integer.

  Returns:
    The GCD of a and b.
  """
  while(b):
    a, b = b, a % b
  return a

# Let's test it out
num1 = 48
num2 = 18
gcd_result = gcd_loop(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")

num3 = 12
num4 = 30
gcd_result_2 = gcd_loop(num3, num4)
print(f"The GCD of {num3} and {num4} is: {gcd_result_2}")

num5 = 7
num6 = 13
gcd_result_3 = gcd_loop(num5, num6)
print(f"The GCD of {num5} and {num6} is: {gcd_result_3}")