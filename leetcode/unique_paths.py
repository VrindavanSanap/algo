def unique_paths(m, n):
  if m == 1 or n == 1:
    return 1
  return unique_paths(m, n - 1) + unique_paths(m - 1, n)


print(unique_paths(3, 7))
