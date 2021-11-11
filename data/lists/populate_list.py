def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions

def menu():

  print("\nPlease select a direction: \n")

  d = directions()

  for index in range(len(d)):
    print(f"{index}: {d[index]}")

  choice = int(input("\nChoice: "))

  if choice == 0:
    return d[0]
  elif choice == 1:
    return d[1]
  elif choice == 2:
    return d[2]
  elif choice == 3:
    return d[3]
  else:
    print("The option is not valid.\n")

def run():
  route = []

  print("Working out escape route...")

  for i in range(0,5):
    route.append(menu())

  print(f"Escape route: {route}")

run()