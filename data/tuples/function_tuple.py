def likelihood():
  likelihoods = (50, 38, 27, 99, 4)

  return (min(likelihoods), max(likelihoods))

def run():
  minimum = likelihood()[0]
  maximum = likelihood()[1]

  print(f"Minimum likelihood of falling: {minimum}%")
  print(f"Maximum likelihood of falling: {maximum}%")

run()