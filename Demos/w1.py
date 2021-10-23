name = input("Insert your name? ")
job = input("What is you occupation? ")
salary = float(input("How much do you earn? "))

salary = salary - 0.1*salary

#f let you have a space between sentences
print ("Your name is {}. Do you like your job as a {}? Your salary is reduced, it is now {}".format(name, job, salary))