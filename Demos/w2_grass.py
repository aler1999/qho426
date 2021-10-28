
perfect_height = float(input("What is the perfect grass height? (in cm)"))
current_height = float(input("What is the height of grass at the moment (in cm)"))

counter = 0

if current_height <= perfect_height:
  print("Do not cut the grass, let it grow")
else:
  while perfect_height < current_height:
    print ("Chop-chop number {}".format(counter))
    counter += 1
    current_height *= 0.95
    print("Now the grass is {:.2f}cm tall".format(current_height))