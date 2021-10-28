
cover_type = input("\nWhat type of cover does the book have?\n")

while cover_type != "soft" and cover_type != "Soft" and cover_type != "hard" and cover_type != "Hard" :
  cover_type = input("The answer can only be 'hard' or 'soft'\n What type of cover does the book have? \n")

if cover_type == "soft" or cover_type == "Soft" :
  is_bound = input("Is the book perfect-bound?\n") 

  if is_bound == "yes" or is_bound == "Yes" :
    print("Soft cover, perfect bound books are very popular!\n")
  else :
    print("Soft covers with coils or stitches are great for short books\n")

elif cover_type == "hard" or cover_type == "Hard" :
  print("Books with hard covers can be more expensive\n")