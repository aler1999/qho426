color1 = {"blue", "yellow", "purple"}

color1.add("black")

print(color1)

#Check membership
if "black" in color1:
  print("Yey")
else:
  print("No")

color2 = {"yellow", "black", "red", "cyan"}

#Union of two sets (without duplicates)
print(color1.union(color2))

#Intersection of two sets, takes the same ones in two sets
print(color1.intersection(color2))

#Difference of two sets, takes only the ones NOT in the other
print(color1.difference(color2))

