#Declare empty list
hated = []

#Declare non-empty list
fav = ["Carbonara", "Pizza", "Casatiello", "Pierogi"]

#Print full list
print(fav)

#Print single element
print(fav[2])

#Add elements at the end of the list
hated.append("Tofu")
hated.append("Beans")
fav.append("Lasagne")

#Appending using a loop and user input
for i in range(2):
  print("Enter another hated dish")
  hated.append(input())

#Insert data at any position on the list
fav.insert(1, "Korma")
fav.insert(3, "Pancakes")

#Print lenght of the list
print(len(hated))

#Remove specific item from the list
fav.remove("Casatiello")

#Remove by index
fav.pop(1)

#Slicing
print(hated[1:3]) 

#Find where pizza is in the list
fav.index('pizza')