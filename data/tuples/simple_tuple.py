def likelihood():
  likelihoods = (50, 38, 27, 99, 4)

  return min(likelihoods)

def run():
  slof = likelihood()

  print(f"Minimum likelihood of falling: {slof}%")

run()