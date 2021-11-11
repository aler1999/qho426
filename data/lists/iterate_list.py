def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions

def menu():
  print("\nPlease select a direction: \n")

  d = directions()

  for index in range(len(d)):
    print(f"{index}: {d[index]}")

def run():
  menu()

run()