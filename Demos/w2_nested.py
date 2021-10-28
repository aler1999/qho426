#nested conditions
salary = float(input("Insert your salary "))
years = int(input("\nHow long have you been in the company "))

if years > 2:
  if salary < 25000:
    salary *= 1.1
  else:
    salary += 100
elif years > 1:
  print("\nNo salary increase for you.")
else:
  if salary < 15000:
    salary = 15000
    print ("\nApologize, there has been an error, your salary is now 20000")

print("\nYour salary is now {:.2f}".format(salary))