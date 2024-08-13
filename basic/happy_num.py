def is_happy(n):
  visited = set()
  while True:
    d0 = n // 100
    d1 = (n // 10) % 10
    d2 = n % 10

    n = d0**2 + d1**2 + d2**2
    print(n)
    if n == 1:
      return True
    if n in visited:
      return False
    visited.add(n)


is_happy(19)
