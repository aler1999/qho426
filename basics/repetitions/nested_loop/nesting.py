print("Please enter a sequence: ")
seq = input()
print("Please enter a character for marker: ")
marker = input()

m1 = 99999
m2 = 99999

for pos in range(len(seq)):
  let = seq[pos]
  if let == marker:
    if m1 == 99999:
      m1 = pos
    elif m2 == 99999:
      m2 = pos

print(f"The distance between the two markers is {m2-m1-1}")