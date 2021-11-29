import csv

def search(file):
  print("\n Searching...")
  data = dict()
  lista = []

  with open(file) as file:
    for line in file:
      a = line.split("\n")
      b = a[0].startswith("Section")

      if b == True:
        s_section = line.rstrip("\n").split(":")
        section = s_section[1]
        lista = []
      
      else:
        lista.append(line.rstrip("\n"))
        data[section] = lista

  print("Done!")

  return data


def run():
  data = search("data/files/txt/books.txt")

  # Open the file in the Write Mode
  with open('data/files/txt/generated.csv', 'w') as file:

    # Create the CSV Writer
    w = csv.writer(file, delimiter = ",")

    # Write rows in the CSV file
    for i in data:
      for e in data[i]:
        w.writerow(list((i, e)))
  
run()