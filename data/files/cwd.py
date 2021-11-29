import os

def cwd():
  # Getting the path of the current directory
  path = os.getcwd()
  print(f"Current Working Directory: {path}")
  print("\nThe directory contains the following:")

  # For each file in the current directory print the file name
  for file in os.listdir(path):
    print(file)

def run():
  print("Processing...")

  cwd()

run()