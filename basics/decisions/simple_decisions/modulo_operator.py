
n = int(input(("Please enter a whole number.\n")))

# Using the modulo operator we can find from the number returned by the function if the number is odd (0) or even (1)

if n % 2 == 0 :
  print("\nThe number {} is an odd number.".format(n))
else :
  print("\nThe number {} is an even number.".format(n))