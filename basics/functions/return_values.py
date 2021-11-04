def sum_weights(weight_Beep, weight_Bop):
  return weight_Beep + weight_Bop

def calc_avg_weight(weight_Beep, weight_Bop):
  return sum_weights(weight_Beep, weight_Bop)/2

def run():
  weight_Beep = float(input("Insert the weight of Beep: "))
  weight_Bop = float(input("Insert the weight of Bop: "))

  operation = input("Would you like to perform a sum or average? ")

  if operation.lower() == "sum":
    print(sum_weights(weight_Beep, weight_Bop))
  elif operation.lower() == "average":
    print(calc_avg_weight(weight_Beep, weight_Bop))

run()