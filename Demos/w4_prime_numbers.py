def isPrime(n):
  for thing in range(2, n):
    if n % thing == 0:
      return False
  return True

def findPrime(s, e):
  for i in range(s, e):
    if isPrime(i):
      return i

def encrypt():
  x = int(input("Provide a starting point: "))
  y = int(input("Provide a end point: "))
  p1 = findPrime(x,y)

  x = int(input("Provide a starting point: "))
  y = int(input("Provide a end point: "))
  p2 = findPrime(x,y)

  return p1*p2

print(encrypt())