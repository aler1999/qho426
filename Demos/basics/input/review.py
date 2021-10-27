print("-----------------------------------------------------------")
print("\nInsert the reference number of the mathematical operation you need")

print("\n1. Calculation of the factorial")
print("\n2. Area of ​​the circle")

answer = int(input())

#Calculation of the factorial
while answer != 1 and answer != 2:
  print("\nYour choice can only be 1 or 2")
  answer = int(input())

if answer == 1:
  print("\nInsert a number")
  number = int(input())
  factorial = 1

  while number > 0:
    factorial = factorial * number
    number = number - 1

  print("\nThe factorial is", factorial)

#Calculation of the area of the circle
if answer == 2:
  print("\nEnter the radius of the circle (in cm)")
  radius = float(input())

  area = (radius ** 2) * 3.141592653589793 

  print("\nThe value of the area of ​​the circle is {}".format(area), "cm2")