def input_word():
  return input("Please, now intert the word: ")

def display_box(word):
  print("-" * (len(word) + 2))
  print("|" + word + "|" )
  print("-" * (len(word) + 2))

def display_lower_case(word):
  print(word.lower())

def display_upper_case(word):
  print(word.upper())

def display_mirrored(word):
  mirror_word = ""
  counter = len(word)
  for i in range(len(word)):
    mirror_word += word[counter-1]
    counter -= 1
  print(mirror_word)

def repeat(word):
  times = int(input("How many times should I repeat the word? "))
  
  for i in range(times):
    if i % 2 == 0:
      print(word.lower())
    else:
      print(word.upper())  

def run():

  print("-------------------------\n")

  a = 1

  while a != 0:

    w = input_word()

    print("Please select from the following options:\n")

    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat\n")

    a = input("Answer: ")

    if a == "1":
      display_box(w)
    elif a == "2":
      display_lower_case(w)
    elif a == "3":
      display_upper_case(w)
    elif a == "4":
      display_mirrored(w)
    elif a == "5":
      repeat(w)

run()