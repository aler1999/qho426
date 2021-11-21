def simple_tuple():
  #define tuple
  person = ("Alessandro", 22, False)

  print(person)

  print(f"Name: {person[0]} Age: {person[1]}")

  #no mutation possible!
  #person[0] = "Gino"

  #tuples can be concatenated (joined)
  p1 = person + (20, "none")
  print(p1)
  print(person)

  t = (3,6,7,4,3,2,7)
  print(max(t))
  print(min(t))

simple_tuple() 