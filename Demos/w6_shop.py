def shop():
  items = {"Fish":1, "Eggs":1.99, "Chips":1.49, "Cheese":4, "Coconut":2.29, "Bread":1.39, "Nesquik":3.39, "Milk":1.59}

  return items

def view_all(products = {}):
  for i,j in products.items():
    print(f"{i}: £{j}")

def basket():
  basket = list()

  while True:
    item = input("\nEnter the item (or \"stop\" to stop): ")

    if item.lower() == "stop":
      break

    quantity = int(input("\nHow many?: "))

    for i in range(quantity):
      basket.append(item)
    
  return basket

def till(basket = []):
  shoplist = shop()
  total = 0.0

  for item in basket:
    total += shoplist[item]
  
  return total

print(till(basket()))