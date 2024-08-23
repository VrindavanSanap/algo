
fibs = {0:1, 1:1}
def fib(n): 
  if n in fibs:
    return fibs[n]
  else:
    fibs[n - 1] = fib(n - 1)
    fibs[n - 2] = fib(n - 2)
    return fibs[n - 1] + fibs[n - 2]

for i in range(2, 100):
  print(i, fib(i))
