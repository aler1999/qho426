def observed():
  observations = []

  for i in range(5):
    observations.append(input("Enter an observation:"))
  
  return observations

def remove_observations(observations = []):

  remove = input("Do you wish to remove an observation? y/n: ")

  while remove == "y":
    which = input("Which observation do you wish to remove? -> ")

    observations.remove(which)

    print(which, "has been removed...")
    print(observations)

    remove = input("Do you wish to remove another observation? y/n: ")

def run():
  x = observed()
  remove_observations(x)
  
  # obs_set is a set, no repetitions in a set
  obs_set = set()

  for i in x:
    # Tuplex is a tuple, unique
    tuplex = (i, x.count(i))
    obs_set.add(tuplex)

  for thing in obs_set:
    print(f"{thing[0]} has been observed {thing[1]} times")

run()
