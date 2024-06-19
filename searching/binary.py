#!/usr/bin/python3
import math
data = list(range(1, 11))
def binary_search(data, value):
  l = 0
  r = len(data) - 1
  while(l <= r):
    m = math.floor((l + r) / 2) 
    value_m = data[m]
    print(value_m)
    if (value_m == value):
      return m 
    elif (value_m < value):
      l = m + 1 
    elif (value_m > value):
      r = m - 1

  return -1

res = binary_search(data, 9)
print(f"found at index:{res}")
