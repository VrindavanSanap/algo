from numba import njit
from tqdm import tqdm


@njit
def sum_square_digits(n):
  sum_squares = 0
  while n != 0:
    sum_squares += (n % 10) ** 2
    n //= 10
  return sum_squares


@njit
def digit_chain_recursive(n):
  if n == 0 or n == 1 or n == 89:
    return n
  else:
    return digit_chain_recursive(sum_square_digits(n))


@njit
def digit_chain_iterative(n):
  while True:
    if n == 0 or n == 1 or n == 89:
      return n
    else:
      n = sum_square_digits(n)


def digit_chain_iterative_with_dict(n):
  visited = dict({})
  while True:
    if n == 0 or n == 1 or n == 89:
      return n
    else:
      if n in visited:
        n = visited[n]
      else:
        visited[n] = sum_square_digits(n)


ends_with_89 = 0
ends_with_1 = 0
for i in tqdm(range(10**7)):
  if digit_chain_iterative(i + 1) == 1:
    ends_with_1 += 1
  else:
    ends_with_89 += 1

print(f"{ends_with_1}, {ends_with_89}")
