name = input("Enter your name: ")

if len(name) > 8:
  print("You have a long name, can I use a nickname please?")
elif len(name) <=3:
  print("Your name is very short")
elif name == "Piotr":
  print("That is a boring name!")
print("Nevertheless, welcome to the session {}".format(name))
else
  print("Your name is not too short and not too long")
