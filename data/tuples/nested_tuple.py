def steps():
  likelihoods = [("step 1", 50), 
  ("step 2", 38),
  ("step 3", 27),
  ("step 4", 99),
  ("step 5", 4)]

  return likelihoods

def run():
  s = steps()

  good_steps = []
  bad_steps = []

  for i in range(len(s)):
    if (s[i][1]) >= 50:
      bad_steps.append(s[i])
    else:
      good_steps.append(s[i])

  print(f"Good steps: {good_steps}, Bad steps: {bad_steps}")

run()