count = ""

rows = int(input("How many rows should I have? "))

columns = int(input("\nHow many columns should I have? "))

print("Here I go:\n")

for count in range(0, rows):
    for number in range(0, columns):
        print(":D", end="")
    print()

print("\nDone!")