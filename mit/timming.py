import time


def c_to_f(c):
  return c * 9 / 5 + 32


def bob_sum(n):
  sum_ = 0
  for i in range(n):
    sum_ += i
  return sum_


def bob_square(n):
  square = 0
  for i in range(n):
    for j in range(n):
      square += 1
  return square


def time_wrapper(f, L):
  print("Timing", f.__name__)
  for i in L:
    t = time.time()
    print(f(i))
    dt = time.time() - t 
    f(i)
    dt = time.time() - t
    print(f"{f.__name__} ({i} took {dt} sec)")


L_N = [1]
for i in range(8):
  L_N.append(L_N[-1] * 10)

time_wrapper(c_to_f, L_N)
time_wrapper(bob_sum, L_N)
time_wrapper(bob_square, L_N)
