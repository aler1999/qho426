phrase = input("What phrase do you see? ")

p_reversed = ""
c_reversed = ""

print("\nReversing...\n")

for characters in phrase:
  c_reversed = characters + p_reversed
  
print("The phrase is: " + p_reversed) 

#NOT WORKING