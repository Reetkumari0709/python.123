def is_prime(num):
  """Checks if a number is prime.

  Args:
    num: An integer greater than 1.

  Returns:
    True if num is prime, False otherwise.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def find_primes_in_range(start, end):
  """Finds and prints all prime numbers within a given range.

  Args:
    start: The starting number of the range (inclusive).
    end: The ending number of the range (inclusive).
  """
  prime_numbers = []
  for num in range(start, end + 1):
    if is_prime(num):
      prime_numbers.append(num)
  if prime_numbers:
print(f"Range: {', '.join(map(str, prime_numbers))}")
  else:
    print(f"No prime numbers found in the range: {start} to {end}")

# Get input from the user
start_range = int(input("Starting: "))
end_range = int(input("Ending: "))

# Find and print prime numbers in the given range
find_primes_in_range(start_range, end_range)