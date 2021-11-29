def search(file):
  print("\nSearching...\n")

  with open(file) as file:
    for line in file:
      print(f"Looked in {line}")
  
  print("\n...Done!")

def run():
  search("data/files/txt/locations.txt")

run()