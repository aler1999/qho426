
n = int(input(("Please enter a whole number.\n")))

# Using the modulo operator we can find from the number returned by the function if the number is even (0) or odd (1)

if n % 2 == 0 :
  print("\nThe number {} is an even number.".format(n))
else :
  print("\nThe number {} is an odd number.".format(n))