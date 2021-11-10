phrase = input("What phrase do you see? ")
p_reversed = ""

print("\nReversing...\n")

for i in range((len(phrase)-1), -1, -1):
  p_reversed += phrase[i]

print("The phrase is: " + p_reversed)