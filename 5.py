print("Numbers between 1 and 100 divisible by 7 but not by 5:")
for number in range(1, 101):
  if number % 7 == 0 and number % 5 != 0:
    print(number);