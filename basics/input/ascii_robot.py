def build_robot(x):
  # Display head 
  print("\t\t  ##############") 
  print("\t\t  #            #") 
  print("\t\t###  {}      {}  ###".format(x, x)) 
  print("\t\t###   ------   ###") 
  print("\t\t  #            #") 
  print("\t\t  ##############")

  # Display chest 
  print("\t\t    ##########") 
  print("\t\t####          ####")
  print("\t\t#  #  ######  #  #")
  print("\t\t#  #    #     #  #")
  print("\t\t#  ##        ##  #")
  print("\t\t ##  #      #  ## ")
  print("\t\t      ######")

print("Please enter a character for the eye")
eyes = input()

while len(eyes) != 1 :
  print("You can only insert one character!")
  print("Please enter a character for the eye")
  eyes = input()
else:
  build_robot(eyes)