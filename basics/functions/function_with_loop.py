def cross_bridge(steps):

  distance = 0

  for i in range(steps):
    print("Crossed step")
    distance += 1

  if distance > 5:
    print("The bridge is collapsing!")
  else:
    print("we must keep going!")

cross_bridge(3)
cross_bridge(6)