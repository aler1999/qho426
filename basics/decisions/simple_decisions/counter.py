
odd_numbers = 0
even_numbers = 0

i = 0

while i < 3 :
  n = int(input("\nPlease enter a whole number.\n"))

  if n % 2 == 0 :
   odd_numbers += 1
  else :
    even_numbers += 1

  i += 1

print ("There were {} even and {} odd numbers.".format(odd_numbers, even_numbers))