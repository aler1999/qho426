def search(file):
  print("\nSearching...\n")

  # Definition of empty lists
  sections = []
  books = []

  with open(file) as file:
    for line in file:
      a = line.split("\n")
      b = a[0].startswith("Section")

      if b == True:
        #print(a)
        c = line.rstrip("\n").split(":")
        #print(c)
        sections.append(c[1])
        #print(sections)
      else:
        x = line.rstrip("\n")
        books.append(x)

    print("Done!")

  return (sections, books)

def save(file, tuplex):
  print("Saving...")

  with open(file, "w") as file:
    file.write(f"Sections: {tuplex[0]}")
    file.write(f"\nBooks: {tuplex[1]}")

    print("Done!")

def run():
  data = search("data/files/txt/books.txt")

  save("data/files/txt/books.txt", data)

run()