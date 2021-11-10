bri = "**"

req = int(input("What level of brightness is required? "))

print("\nAdjusting brightness...\n")

for i in range(0, req, 2):
  print(f"Beep's brightness level: {bri}\nBop's brightness level: {bri}\n")
  bri += "**"
