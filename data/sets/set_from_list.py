def observed():
  observations = []

  for i in range(7):
    observations.append(input("Enter a value: "))

  return observations

def run():
  print("Counting observations...")

  observations = observed()

  observations_set = set()
  
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

  # display set
  for data in observations_set:
    print(f"{data[0]} observed {data[1]} times.")

run()

#DID WITH SOLUTIONS