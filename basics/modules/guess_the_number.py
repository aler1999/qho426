import random as rnd

mini = int(input("Please enter the minimum value:\n"))
maxi = int(input("\nPlease enter the maximum value:\n"))

if mini < maxi:
  n_guessed = 999999999999999999999999999999
  n_guess = rnd.randrange(mini, maxi)

  print("\nI am thinking of a number between {} and {}. Can you guess what it is?".format(mini, maxi))

  while n_guess != n_guessed:
    n_guessed = int(input())

    if n_guess > n_guessed:
      print("\nYour guess is too low. \nTry again:")

    if n_guess < n_guessed:
      print("\nYour guess is too high. \nTry again:")
    
    if n_guess == n_guessed:
      print("\nCongratulations! You guessed my number!")

else:
  print("The minimum number can't be higher than the maximum.")