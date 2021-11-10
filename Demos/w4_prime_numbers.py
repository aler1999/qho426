def isPrime(n):
  for thing in range(2, n):
    if n % thing == 0:
      return False
    else:
      return True