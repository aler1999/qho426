#Initialize empty Dictionary
phonebook = {}
d2 = dict()

#Initialize no empty dictionary
alessandro_data = {"Name": "Alessandro", "Age": "22", "Doggo": "False", "Title": "Mr"}

print(alessandro_data)

#Print a part of dictionary for printing purpose
x = alessandro_data["Name"]
y = alessandro_data["Age"]
print(f"{x} is {y} years old.")

#Adding elements to a dictionary
phonebook["Max"] = "+44 9876789877"
phonebook["Uga"] = "+95 6634235933"
phonebook["Lucy"] = None

print(phonebook)

#Add more people in the phone book
for i in range(3):
  name = input("Enter the name: ")
  number = input("Enter the number: ")
  phonebook[name] = number

name = input("Who would you like to call? ")

if name in phonebook:
  print(f"Calling {name} with phone number {phonebook[name]}")
else:
  print("Number not found")