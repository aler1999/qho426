import random as rnd

mini = int(input("Please enter the minimum value: "))
maxi = int(input("Please enter the maximum value:"))

n_guessed = 999999999999999999999999999999
n_guess = rnd.randrange(mini, maxi)

while(n_guess != n_guessed):
  int(input("I am thinking of a number between {} and {}.  Can you guess what it is?".format(mini, maxi)))