def dimension():
  l = float(input("Insert the lenght of the room: "))
  w = float(input("Insert the widht of the room: "))
  return l,w

def calc_area(l, w):
  return l*w

def name_room():
  return input("Insert the name of the room: ")

def price(name,area):
  if name.lower() == "bedroom":
    return 20 * area
  elif name.lower() == "bathroom":
    return 12 * area
  elif name.lower() == "kitchen":
    return 15 * area
  else: 
    return 55 * area

def run():
  total_price = 0.0
  num = int(input("How many rooms would you like to paint? "))

  for i in range(num):
    n = name_room()
    lenght, width = dimension()
    area = calc_area(lenght, width)
    total_price += price(n, area)

  print("The total price to be charged is £{}".format(total_price))

run()